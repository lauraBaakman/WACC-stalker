""" . """
from flask.ext.restful import Resource, reqparse, request
from flask import make_response
from bson.json_util import dumps

import database as db


class SearchResource(Resource):

    """ Resources class. """

    parser = None

    def get(self):
        """
            HTTP GET request.
            Parameters:
                None
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
        import pdb
        try:
            # pdb.set_trace()
            json = request.json
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

    def init_parser(self):
        """ Initialize the parser. """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('stalker', type=str)
        self.parser.add_argument('location', type=str)
        self.parser.add_argument('victim', type=str)

    def __init__(self):
        """ Initialize the Resource. """
        self.init_parser()


class StalkerResource(Resource):

    """ Resource class. """

    stalker = {
        'facebook_id': None,
        'relationship_status': None,
        'birthdate': None,
        'gender': None,
        'linkedIn_id': None,
        'industry': None
    }

    parser = None

    def get(self):
        """ . """
        return self.stalker

    def post(self):
        """ . """
        args = self.parser.parse_args()
        for key in self.stalker.iterkeys():
            self.stalker[key] = args[key]

        return "Received Stalker", 201

    def init_parser(self):
        """ . """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('facebook_id', type=str)
        self.parser.add_argument('relationship_status', type=str)
        self.parser.add_argument('birthdate', type=str)
        self.parser.add_argument('gender', type=str)
        self.parser.add_argument('linkedIn_id', type=str)
        self.parser.add_argument('industry', type=str)

    def __init__(self):
        """ . """
        self.init_parser()


class VictimResource(Resource):

    """ Resource class. """

    victim = {
        'facebook_id': None
    }

    parser = None

    def get(self):
        """ . """
        return self.victim

    def post(self):
        """ . """
        args = self.parser.parse_args()
        self.victim['facebook_id'] = args['facebook_id']
        return "Received victim", 201

    def init_parser(self):
        """ . """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('facebook_id', type=str)

    def __init__(self):
        """ . """
        self.init_parser()

if __name__ == '__main__':
    print api.connection.wacc.searches.find()
