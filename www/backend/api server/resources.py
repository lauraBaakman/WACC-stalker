""" . """
from flask.ext.restful import Resource, fields, marshal, reqparse
from flask import make_response
from bson.json_util import dumps
from bson import ObjectId
import pymongo

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
            'latitude',
            required=True,
            type=float,
            location='json',
            help='latitude is required'
        )
        self.req_parser.add_argument(
            'longitude',
            required=True,
            type=float,
            location='json',
            help='longitude is required'
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
        except Exception, e:
            print e
            status_code = 500
            response = {'message': 'Something went terribly wrong.', 'status': status_code}

        return make_response(dumps(response), status_code)

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                stalker_id:        required, string
                latitude:                required, float
                longitude:               required, float
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
            search.location['lat'] = args['latitude']
            search.location['long'] = args['longitude']
            search.location['country_code'] = args['country_code']

            # Optional parameters
            search.victim_id = args['victim_id']

            search.save()

            data = str(search['_id'])
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
            'victim_id',
            required=True,
            location='json',
            type=unicode,
            help='victim_id is required'
        )

    def put(self, id):
        """
        HTTP PUT method to update a search with a victim.

        The victim needs to be created and must be provides as victim_id
        """
        message = "OK"
        status_code = 200

        try:
            # Parsing update information from json
            args = self.req_parser.parse_args()

            # Retrieving the search given in the url
            search = db.connection.wacc.searches.Search.find_one({'_id': ObjectId(id)})

            if search is not None:
                search.victim_id = args['victim_id']
                search.save()
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
        except Exception, e:
            print e
            status_code = 500
            response = {'message': 'Something went terribly wrong.', 'status': status_code}

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
            response_msg = "Internal server error....."

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
        except Exception, e:
            print e
            status_code = 500
            response = {'message': 'Something went terribly wrong.', 'status': status_code}

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
            print e
            status_code = 500
            response_msg = "Internal server error."

        return {'message': response_msg, 'status': status_code}, status_code


def get_by_method(method, output_fields, sort_x=None, limit_x=0, scope=None):
    """
    HTTP GET request.

    Parameters:
        None
    Return codes:
        500:    Internal Server Error
        200:    Everything is shiny
        204:    No results
    """
    status_code = 200
    response = []

    try:
        top_x_results = method(scope).find(sort=sort_x, limit=limit_x)

        for result in top_x_results:
            response.append(marshal(result, output_fields))
    except Exception, e:
        print e
        status_code = 500
        response = {'message': 'Something went terribly wrong.', 'status': status_code}

    return make_response(dumps(response), status_code)


class StatisticsLocationFrequency(Resource):

    """Resource class to get the location frequency."""

    def __init__(self):
        """ . """
        self.output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        self.sort_x = [('_id', pymongo.DESCENDING)]
        self.limit_x = 10

    def get(self):
        """ . """
        return get_by_method(
            mr.search_location_frequency,
            self.output_fields,
            self.sort_x,
            self.limit_x
        )


class StatisticsRelationshipFrequency(Resource):

    """Resource class to get the relationship frequency."""

    def __init__(self):
        """ . """
        self.output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        self.sort_x = [('_id', pymongo.DESCENDING)]
        self.limit_x = 10

    def get(self):
        """ . """
        return get_by_method(
            mr.stalker_relationship_frequency,
            self.output_fields,
            self.sort_x,
            self.limit_x
        )


class StatisticsGenderRelationshipFrequency(Resource):

    """Resource class to get the {gender, relationship} frequency."""

    def __init__(self):
        """ . """
        self.output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        self.sort_x = [('_id', pymongo.DESCENDING)]
        self.limit_x = 10

    def get(self, gender):
        """ . """
        scope = {"gender": gender}

        return get_by_method(
            mr.gender_relationship_frequency,
            self.output_fields,
            self.sort_x,
            self.limit_x,
            scope
        )


class StatisticsGenderLocationFrequency(Resource):

    """Resource class to get the search location and gender of a stalker."""

    def __init__(self):
        """ . """
        self.value_field = {
            'gender': fields.String(attribute='gender'),
            'country_codes': fields.List(fields.String, attribute='country_codes')
        }

        self.output_fields = {
            'term': fields.Nested(self.value_field, attribute='value')
        }

    def get(self):
        """ . """
        return get_by_method(
            mr.gender_location_frequency,
            self.output_fields,
        )
