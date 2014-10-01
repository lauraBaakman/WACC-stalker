""" . """
from flask.ext.restful import Resource, reqparse


class Stalker(Resource):

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
