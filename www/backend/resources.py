""" . """
from flask.ext.restful import Resource, request, fields, marshal, reqparse
from flask import make_response
from bson.json_util import dumps
import pymongo
import itertools
import sys

import database as db
import mapreduce as mr


class SearchesResource(Resource):

    """ Resources class. """

    def __init__(self):
        """ Initialization. """
        self.req_parser = reqparse.RequestParser()
        self.req_parser.add_argument(
            'stalker_id',
            required=True,
            type=unicode,
            location='json',
            help='stalker_id is required'
        )
        self.req_parser.add_argument(
            'lat',
            required=True,
            type=float,
            location='json',
            help='lat is required'
        )
        self.req_parser.add_argument(
            'long',
            required=True,
            type=float,
            location='json',
            help='long is required'
        )
        self.req_parser.add_argument(
            'country_code',
            required=True,
            type=unicode,
            location='json',
            help='country_code is required'
        )
        self.req_parser.add_argument(
            'victim_id',
            required=False,
            default=u'',
            type=unicode,
            location='json',
        )
        super(SearchesResource, self).__init__()

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            200:   Success
        """
        output_location_fields = {
            'lat': fields.Float(attribute='lat'),
            'long': fields.Float(attribute='long'),
            'country_code': fields.String(attribute='country_code')
        }

        output_fields = {
            'stalker_id': fields.String(attribute='stalker_id'),
            'location': fields.Nested(output_location_fields),
            'victim_id': fields.String(attribute='victim_id', default='')
        }

        status_code = 200
        response = []

        try:
            results = db.connection.wacc.searches.find()

            for result in results:
                response.append(marshal(result, output_fields))
        except:
            response = {'message': 'Something went terribly wrong.', 'status': status_code}
            status_code = 500

        return make_response(dumps(response), status_code)

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                stalker_id:        required, string
                lat:                required, float
                long:               required, float
                country_code:       required, three letter string
                victim_id:             optional, string, default: ""
        Return codes:
            500:    Internal server Error
            201:    Created the search object
        """
        status_code = 201
        response_msg = "OK: Received search"
        data = None

        try:
            args = self.req_parser.parse_args()

            search = db.connection.Search()

            search.stalker_id = args['stalker_id']
            search.location['lat'] = args['lat']
            search.location['long'] = args['long']
            search.location['country_code'] = args['country_code']

            # Optional parameters
            search.victim_id = args['victim_id']

            search.save()

            search_id = search['_id']
            data = str(search_id[0])
        except Exception, e:
            print e
            status_code = 500
            response_msg = "Internal server error."

        return {'message': response_msg, 'data': data, 'status': status_code}, status_code


class SearchResource(Resource):

    """ Search update resource. """

    def __init__(self):
        """ Initialization. """
        self.req_parser = reqparse.RequestParser()
        self.req_parser.add_argument(
            'vicitm_id',
            required=True,
            location='json',
            help='victim_id is required'
        )

    def put(self, id):
        """
        HTTP PUT method to update a search with a victim.

        The victim needs to be created and must be provides as victim_id
        """
        message = "OK"
        status_code = 200

        connection = db.connetion.Search()

        try:
            # Parsing update information from json
            args = self.req_parser.parse_args()

            # Retrieving the search given in the url
            search = connection.get_from_id(id)

            if search is not None:
                search.victim_id = args['victim_id']
            else:
                status_code = 404
                message = "Search with id does not exist."

        except Exception, e:  # MultipleResultsFound
            print e
            status_code = 500
            message = "Internal server error."

        return {'message': message, 'status': status_code}, status_code


class StalkersResource(Resource):

    """ Resource class. """

    def __init__(self):
        """ Initialization. """
        self.req_parser = reqparse.RequestParser()
        self.req_parser.add_argument(
            'stalker_id',
            required=True,
            type=unicode,
            location='json',
            help='stalker_id is required'
        )
        self.req_parser.add_argument(
            'relationship_status',
            required=False,
            default=u'',
            type=unicode,
            location='json',
            help='relationshipt_status is required'
        )
        self.req_parser.add_argument(
            'birthdate',
            required=True,
            type=unicode,
            location='json',
            help='birthdate is required'
        )
        self.req_parser.add_argument(
            'gender',
            required=True,
            type=unicode,
            location='json',
            help='gender is required'
        )
        self.req_parser.add_argument(
            'linkedIn_id',
            required=False,
            default=u'',
            type=unicode,
            location='json'
        )
        self.req_parser.add_argument(
            'industry',
            required=False,
            default=u'',
            type=unicode,
            location='json'
        )

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            200:   Success
        """
        output_fields = {
            'stalker_id': fields.String(attribute='stalker_id'),
            'relationship_status': fields.String(attribute='relationship_status', default=''),
            'birthdate': fields.String(attribute='birthdate'),
            'gender': fields.String(attribute='gender'),
            'linkedIn_id': fields.String(attribute='linkedIn_id', default=''),
            'industry': fields.String(attribute='industry', default='')
        }

        status_code = 200
        response = []

        try:
            results = db.connection.wacc.stalkers.find()

            for result in results:
                response.append(marshal(result, output_fields))
        except:
            response = {'message': 'Something went terribly wrong.', 'status': status_code}
            status_code = 500

        return make_response(dumps(response), status_code)

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                stalker_id:             required, string
                relationship_status:    optional, string, default: ''
                birthdate:              required, string
                gender:                 required, string
                linkedIn_id:            optional, string, default: ''
                industry:               optional, string, default: ''
        Return codes:
            500:    Internal server Error
            201:    Created the stalker object
        """
        status_code = 201
        response_msg = 'OK: Received stalker.'

        try:
            args = self.req_parser.parse_args()

            stalker = db.connection.Stalker()

            # Required parameters
            stalker.stalker_id = args['stalker_id']
            stalker.birthdate = args['birthdate']
            stalker.gender = args['gender']

            # Optional parameters
            stalker.linkedIn_id = args['linkedIn_id']
            stalker.industry = args['industry']
            stalker.relationship_status = args['relationship_status']

            stalker.save()
        except Exception, e:
            print e
            status_code = 500
            response_msg = "Internal server error."

        return {'message': response_msg, 'status': status_code}, status_code


class VictimsResource(Resource):

    """ Resource class. """

    def __init__(self):
        """ Initialization. """
        self.req_parser = reqparse.RequestParser()
        self.req_parser.add_argument(
            'victim_id',
            required=True,
            type=unicode,
            location='json',
            help='Victim_id is a required string'
        )

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            200:   Success
        """
        output_fields = {
            'victim_id': fields.String(attribute='victim_id')
        }

        status_code = 200
        response = []

        try:
            results = db.connection.wacc.victims.find()

            for result in results:
                response.append(marshal(result, output_fields))
        except:
            response = {'message': 'Something went terribly wrong.', 'status': status_code}
            status_code = 500

        return make_response(dumps(response), status_code)

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                victim_id:      required, unicode
        Return codes:
            500:    Internal server Error
            201:    Created the victim object
        """
        status_code = 201
        response_msg = 'OK: Received victim.'

        try:
            args = self.req_parser.parse_args()

            victim = db.connection.Victim()

            victim.victim_id = args['victim_id']

            victim.save()
        except Exception, e:
            status_code = 500
            response_msg = "Internal server error."

        return {'message': response_msg, 'status': status_code}, status_code


class StatisticsLocationFrequency(Resource):

    """Resource class to get the location frequency."""

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            500:    Internal Server Error
            200:    Everything is shiny
            204:    No results
        """
        # Limit the result TODO: make this configurable.
        x = 10

        # Filters the result to more appropriate output form.
        output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        # Response list and status code
        status_code = 200
        response = []

        try:
            # Sort the result DESCENDING and limit it to the first x results.
            top_x_results = mr.search_location_frequency().find(
                limit=x, sort=[('value', pymongo.DESCENDING)]
            )

            # Marshal every document with output_fields.
            for result in top_x_results:
                response.append(marshal(result, output_fields))
        except:  # TODO: return 204 or 500 when relevant
            response = {'message': 'Something went terribly wrong.', 'status': status_code}
            status_code = 500

        return make_response(dumps(response), status_code)


class StatisticsRelationshipFrequency(Resource):

    """Resource class to get the relationship frequency."""

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            500:    Internal Server Error
            200:    Everything is shiny
            204:    No results
        """
        x = 10

        output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        status_code = 200
        response = []

        try:
            top_x_results = mr.stalker_relationship_frequency().find(
                limit=x, sort=[('value', pymongo.DESCENDING)]
            )

            for result in top_x_results:
                response.append(marshal(result, output_fields))
        except:
            response = {'message': 'Something went terribly wrong.', 'status': status_code}
            status_code = 500

        return make_response(dumps(response), status_code)
