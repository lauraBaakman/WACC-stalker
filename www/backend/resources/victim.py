""" . """
from flask.ext.restful import Resource, reqparse


class Victim(Resource):

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
