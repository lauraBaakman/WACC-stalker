""" . """
from flask import Flask
from flask.ext.restful import reqparse, Api, Resource

# Create api
app = Flask(__name__)
api = Api(app)


def abort():
    """ Throw a 404 error code and abort.  """
    abort(404, message="Abort")

# Used to parse arguments from PUT and POST messages?
parser = reqparse.RequestParser()
parser.add_argument('msg', type=str)

# Global message variable
message = ""


class HelloWorld(Resource):

    """ Resource class. """

    def get(self):
        """ HTTP GET request. """
        return {'message': message}

    def post(self):
        """ HTTP POST request. """
        args = parser.parse_args()
        global message
        message = args['msg']
        return '', 201

# Set up of the actual routing
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
