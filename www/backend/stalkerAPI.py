""" . """
from flask import Flask
from flask.ext.restful import Api
from resources import SearchResource, VictimResource, StalkerResource
from models import Stalker, Search, Victim

import database as db

# Create api
app = Flask(__name__)

#app.config.from_object(__name__)
api = Api(app)

# Register the Models.
db.init()
db.connection.register([Stalker, Search, Victim])

import test_data as td

td.clear(db.connection)
td.populate(db.connection)

# Set up of the actual routing
api.add_resource(SearchResource, '/search')
api.add_resource(VictimResource, '/victim')
api.add_resource(StalkerResource, '/stalker')

if __name__ == '__main__':
    app.run(debug=True)
