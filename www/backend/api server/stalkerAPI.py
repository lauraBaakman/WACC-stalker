""" . """
from flask import Flask, request
from flask.ext.restful import Api
from flask.ext.cors import CORS
import sys
import optparse

from resources import *
from models import Stalker, Search, Victim

import database as db

# Create api
app = Flask(__name__)

#app.config.from_object(__name__)
api = Api(app)
cors = CORS(app)


@app.after_request
def add_cors(resp):
    """
    Ensure all responses have the CORS headers. This ensures any
    failures are also accessible by the client.

    source: http://mortoray.com/2014/04/09/allowing-unlimited-access-with-cors/
    """
    resp.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization'
    )
    # set low for debugging
    if app.debug:
        resp.headers['Access-Control-Max-Age'] = '1'
    return resp

# Register the Models.
db.init()
# db.init_replicas()
db.connection.register([Stalker, Search, Victim])

# Set up of the actual routing
api.add_resource(
    SearchesResource,
    '/searches'
)

api.add_resource(
    SearchResource,
    '/search/<string:id>'
)

api.add_resource(
    VictimsResource,
    '/victims'
)

api.add_resource(
    StalkersResource,
    '/stalkers'
)

api.add_resource(
    StatisticsLocationFrequency,
    '/statistics/location/frequency'
)

api.add_resource(
    StatisticsRelationshipFrequency,
    '/statistics/relationship/frequency'
)

api.add_resource(
    StatisticsGenderRelationshipFrequency,
    '/statistics/gender/relationship/frequency/<string:gender>'
)

api.add_resource(
    StatisticsGenderLocationFrequency,
    '/statistics/gender/location/frequency'
)

# Argument parser
parser = optparse.OptionParser(description='Stalker REST Api')

parser.add_option(
    '-t', '--test',
    action="store_true", dest="test", default=False,
    help="when provided the api will generate test data. [default: %default]"
)

parser.add_option(
    '-H', '--host',
    action="store", type="string", dest="host", default="127.0.0.1",
    help="sets host address. [default: %default]"
)

parser.add_option(
    '-p', '--port',
    action="store", type="int", dest="port", default="8000",
    help="set port for the host address. [default: %default]"
)

if __name__ == '__main__':

    options, args = parser.parse_args()
    print 'Test:', options.test

    # import test_data as td
    # td.clear(db.connection)

    # if(len(sys.argv) > 1):
        # print "Generating new test data"
        # Generate test data
        # td.clear(db.connection)
        # td.populate(db.connection)
    app.run(host="127.0.0.1", port=int("5000"), debug=True)
