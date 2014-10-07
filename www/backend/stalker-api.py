""" . """
from flask import Flask
from flask.ext.restful import Api
from resources import SearchResource, VictimResource, StalkerResource
from models import Stalker
import database as db
#from models import Stalker
#from database import Db



# Create api
app = Flask(__name__)
#app.config.from_object(__name__)
api = Api(app)

# Register the Models.
#db.init(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
#db.connection.register([Stalker])
connection = db.init()
connection.register([Stalker])

#stalker = connection.Stalker()
#stalker.facebook_id = "HALLO"
#stalker.save()

# Set up of the actual routing
api.add_resource(SearchResource, '/search')
api.add_resource(VictimResource, '/victim')
api.add_resource(StalkerResource, '/stalker')

if __name__ == '__main__':
    app.run(debug=True)
