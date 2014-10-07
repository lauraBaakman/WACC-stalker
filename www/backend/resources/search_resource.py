""" . """
from flask.ext.restful import Resource, reqparse


class SearchResource(Resource):

    """ Resource class. """

    search = {
        'stalker': None,
        'location': None,
        'victim': None,
        'time': None
    }

    parser = None

    def get(self):
        """ HTTP GET request. """
        # TODO: Remove this function. DEBUG purpose only.
        return self.search

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
