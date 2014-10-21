""" . """
from flask import Flask, request
from flask.ext.restful import Api
from flask.ext.cors import CORS
import sys

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
#db.init_replicas()
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
    '/statistics/gender/location/frequency/<string:gender>'
)

if __name__ == '__main__':
    import test_data as td
    td.clear(db.connection)

    if(len(sys.argv) > 1):
        print "Generating new test data"
        # Generate test data
        td.clear(db.connection)
        td.populate(db.connection)
    app.run(debug=True)
