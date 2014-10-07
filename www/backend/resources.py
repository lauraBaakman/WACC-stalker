""" . """
from flask.ext.restful import Resource, request
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
        #import pdb
        try:
            # pdb.set_trace()
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
        try:
            json = request.json

            stalker = db.connection.Stalker()

            # Required parameters
            stalker.stalker_id = json['stalker_id']
            stalker.relationship_status = json['relationship_status']
            stalker.birthdate = json['birthdate']
            stalker.gender = json['gender']

            # Optional parameters
            stalker.linkedIn_id = json.get('linkedIn_id', u'')
            stalker.industry = json.get('industry', u'')

            stalker.save()
        except Exception, e:
            print e
            return 'Internal Server Error', 500
        return 'Received stalker', 201

    def put(self, stalker_id):



class VictimResource(Resource):

    """ Resource class. """

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
        #import pdb
        try:
            # pdb.set_trace()
            json = request.json

            victim = db.connection.Victim()

            # Required parameters
            victim.victim_id = json['victim_id']

            victim.save()
        except Exception, e:
            print e
            return 'Internal Server Error', 500
        return 'Received victim', 201
