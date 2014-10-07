""" . """
from flask import Flask
from flask.ext.restful import Api
from resources import SearchResource, VictimResource, StalkerResource
from models import Stalker
from database import db

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# Create api
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

# Register the Models.
db.init(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
db.connection.register([Stalker])

stalker = db.connection.Stalker()
stalker.facebook_id = "asdfasdfjkj3239jaidf"
stalker.save()

# Set up of the actual routing
api.add_resource(SearchResource, '/search')
api.add_resource(VictimResource, '/victim')
api.add_resource(StalkerResource, '/stalker')

if __name__ == '__main__':
    app.run(debug=True)
