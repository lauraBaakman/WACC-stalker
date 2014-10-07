""" . """
from flask.ext.restful import Resource, reqparse, fields, marshal_with
import database as db

import json
from bson import json_util
#import bson.json_util as bsjs


class SearchResource(Resource):

    """ Resource class. """

    search = {
        'stalker': None,
        'location': None,
        'victim': None,
        'time': None
    }

    search_fields = {
        'stalker_id': fields.String,
        'victim_id': fields.String
    }

    parser = None

    def get(self):
        """ HTTP GET request. """
        # TODO: Remove this function. DEBUG purpose only.
        cursor = db.connection.wacc.searches.find()

        json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]

        return json_docs

    def post(self):
        """ HTTP POST request. """
        args = self.parser.parse_args()
        for key in self.search.iterKey():
            self.search[key] = args[key]

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