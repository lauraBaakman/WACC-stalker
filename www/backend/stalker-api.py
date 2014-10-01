""" . """
from flask import Flask
from flask.ext.restful import Api
from resources import Search, Victim, Stalker

# Create api
app = Flask(__name__)
api = Api(app)


def abort():
    """ Throw a 404 error code and abort.  """
    abort(404, message="Abort")

# Set up of the actual routing
api.add_resource(Search, '/search')
api.add_resource(Victim, '/victim')
api.add_resource(Stalker, '/stalker')

if __name__ == '__main__':
    app.run(debug=True)
