""" . """
from flask import Flask
from flask.ext.restful import reqparse, Api, Resource
from mongokit import Connection, Document

# Configuration MongoDB
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# Create api
app = Flask(__name__)
api = Api(app)

# Connect to database
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])


def abort():
    """ . """
    abort(404, message="Abort")

parser = reqparse.RequestParser()
parser.add_argument('msg', type=str)

message = ""


class HelloWorld(Resource):

    """ . """

    def get(self):
        """ . """
        return {'message': message}

    def post(self):
        """ . """
        args = parser.parse_args()
        global message
        message = args['msg']
        return '', 201


api.add_resource(HelloWorld, '/')


def max_length(length):
    """ . """
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate


class User(Document):

    """ . """

    structure = {
        'name': unicode,
        'email': unicode,
    }
    validators = {
        'name': max_length(50),
        'email': max_length(120)
    }
    use_dot_notation = True

    def __repr__(self):
        """ . """
        return '<User %r>' % (self.name)

# register the User document with our current connection
connection.register([User])


if __name__ == '__main__':
    app.run(debug=True)
