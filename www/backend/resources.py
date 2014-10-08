""" . """
from flask.ext.restful import Resource, request, reqparse
from flask import make_response
from bson.json_util import dumps

import database as db


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
        statusCode = 200
        resp = make_response(dumps(cursor), statusCode)
        return resp

    def post(self):
        """
            HTTP POST request.
            Parameters:
                JSon object with the keys:
                    stalker:    required, string
                    lat:        required, float
                    long:       required, float
                    victim:     optional, string, default: ""
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
        import pdb
        pdb.set_trace()
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
        cursor = db.connection.wacc.victims.find()
        statusCode = 200
        resp = make_response(dumps(cursor), statusCode)
        return resp


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
        try:
            args = self.req_parser.parse_args()
            #json = request.json

            victim = db.connection.Victim()

            # Required parameters
            victim.victim_id = args['victim_id']

            victim.save()
        except Exception, e:
            print e
            return 'Internal Server Error', 500
        return 'Received victim', 201
