""" . """
from flask.ext.restful import Resource, request, fields, marshal, reqparse
from flask import make_response
from bson.json_util import dumps
import pymongo
import itertools
import sys

import database as db
import mapreduce as mr


class SearchResource(Resource):

    """ Resources class. """

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            200:   Success
        """
        cursor = db.connection.wacc.searches.find()
        print cursor
        statusCode = 200
        resp = make_response(dumps(cursor), statusCode)
        return resp

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                stalker:        required, string
                lat:            required, float
                long:           required, float
                country_code:   required, three letter string
                victim:         optional, string, default: ""
        Return codes:
            500:    Internal server Error
            201:    Created the search object
        """
        try:
            json = request.json
            print json
            search = db.connection.Search()
            search.stalker_id = json['stalker']
            search.location['lat'] = json['lat']
            search.location['long'] = json['long']
            search.location['country_code'] = json['country_code']

            # Optional parameters
            search.victim_id = json.get('victim', u'')
            search.save()
        except Exception, e:
            print e
            return 'Internal Server Error', 500
        return 'Received search', 201

    def put(self, search_stalker_id):
        """ HTTP PUT request. """
        # TODO if there is a db.
        return search_stalker_id, 201


class StalkerResource(Resource):

    """ Resource class. """

    def get(self):
        """
        HTTP GET request.

        Parameters:
            None
        Return codes:
            200:   Success
        """
        cursor = db.connection.wacc.stalkers.find()
        statusCode = 200
        resp = make_response(dumps(cursor), statusCode)
        return resp

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                stalker_id:             required, string
                relationship_status:    required, string
                birthdate:              required, string
                gender:                 required, string
                linkedIn_id:            optional, string, default: ''
                industry:               optional, string, default: ''
        Return codes:
            500:    Internal server Error
            201:    Created the stalker object
        """
        #import pdb
        #pdb.set_trace()
        try:
            json = request.json

            stalker = db.connection.Stalker()

            # Required parameters
            stalker.stalker_id = json['stalker_id']
            stalker.birthdate = json['birthdate']
            stalker.gender = json['gender']

            # Optional parameters
            stalker.linkedIn_id = json.get('linkedIn_id', u'')
            stalker.industry = json.get('industry', u'')
            stalker.relationship_status = json.get('relationship_status', u'')

            stalker.save()
        except Exception, e:
            print e
            return 'Internal Server Error', 500
        return 'Received stalker', 201


class VictimResource(Resource):

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
            response = {'error': 'Something went terribly wrong.'}
            status_code = 500

        return make_response(dumps(response), status_code)

    def post(self):
        """
        HTTP POST request.

        Parameters:
            JSon object with the keys:
                victim_id:      required, string
        Return codes:
            500:    Internal server Error
            201:    Created the victim object
        """

        status_code = 201
        response = "OK: Received victim"

        try:
            args = self.req_parser.parse_args()

            victim = db.connection.Victim()

            # Required parameters
            victim.victim_id = args['victim_id']

            victim.save()
        except Exception, e:
            response = "Internal Server Error"
            status_code = 500

        return response, status_code


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
        x = 10;
        
        # Filters the result to more appropriate output form.
        output_fields = {
            'count': fields.Integer(attribute='value'),
            'term': fields.String(attribute='_id')
        }

        # Response list and status code 
        response = []
        status_code = 200

        try:
            # Sort the result DESCENDING and limit it to the first x results. 
            top_x_results = mr.search_location_frequency().find(limit=x, sort=[('value', pymongo.DESCENDING)])

            # Marshal every document with output_fields.
            for result in top_x_results:
                response.append(marshal(result, output_fields))
        except: # TODO: return 204 or 500 when relevant
            response = {'error': 'Something went terribly wrong.'}
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

        response = []
        status_code = 200

        try:
             top_x_results = mr.stalker_relationship_frequency().find(limit=x, sort=[('value', pymongo.DESCENDING)])

             for result in top_x_results:
                response.append(marshal(result, output_fields))
        except:
            response = {'error': 'Something went terribly wrong'}
            status_code = 500

        return make_response(dumps(response), status_code)
