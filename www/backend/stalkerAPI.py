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
db.connection.register([Stalker, Search, Victim])

# Set up of the actual routing
api.add_resource(SearchResource, '/search')
api.add_resource(VictimResource, '/victim')
api.add_resource(StalkerResource, '/stalker')
api.add_resource(StatisticsLocationFrequency, '/statistics/location/frequency')
api.add_resource(StatisticsRelationshipFrequency, '/statistics/relationship/frequency')

if __name__ == '__main__':
    import test_data as td
    td.clear(db.connection)
    
    if(len(sys.argv) > 1):
        print "Generating new test data"
        # Generate test data
        td.clear(db.connection)
        td.populate(db.connection)
    app.run(debug=True)
