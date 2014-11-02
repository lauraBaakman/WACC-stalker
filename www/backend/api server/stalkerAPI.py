""" . """
from flask import Flask, request
from flask.ext.restful import Api
from flask.ext.cors import CORS
import optparse

from resources import *


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
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization'
    )
    # set low for debugging
    if app.debug:
        resp.headers['Access-Control-Max-Age'] = '1'
    return resp

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
parser = optparse.OptionParser(
    description='Stalker REST Api',
    #usage="usage: %prog [options]"
)

parser.add_option(
    '-q', '--quiet',
    action="store_true", dest="quiet", default=False,
    help="be quiet. [default: %default]"
)

# Network groups
network_group = optparse.OptionGroup(
    parser, "Network Options",
    "With these options you can set the network setting. "
)

network_group.add_option(
    '-H', '--host',
    action="store", type="string", dest="host", default="127.0.0.1",
    help="sets host address. [default: %default]"
)

network_group.add_option(
    '-P', '--port',
    action="store", type="int", dest="port", default="8000",
    help="set port for the host address. [default: %default]"
)

network_group.add_option(
    '-r', '--replicaset',
    action="store_true", dest="replicaset",  default=False,
    help="if provided the api will use the replica set provided in config.py. [default: %default]"
)

parser.add_option_group(network_group)

# Development options group
dev_group = optparse.OptionGroup(
    parser, "Dangerous Options",
    "Caution: use these options at your own risk.  "
)
dev_group.add_option(
    '-d', '--debug',
    action="store_true", dest="debug", default=False,
    help="if provided the api will run in debug mode. [default: %default]"
)

dev_group.add_option(
    '-t', '--test',
    action="store_true", dest="generate", default=False,
    help="generate test data. [default: #stalker=500, #victims=200, #searches=700]"
)
dev_group.add_option(
    '-p', '--params',
    action="store", type="int", nargs=3, dest="params",
    help="generate test data with user provided parameters. "
    "[PARAMS: #stalkers #victims #searches]"
)

parser.add_option_group(dev_group)

if __name__ == '__main__':
    import test_data as td

    options, args = parser.parse_args()

    if options.replicaset:
        if not options.quiet:
            print "DATABASE: Using replica set databse connection."
        db.init(True)
    else:
        if not options.quiet:
            print "DATABASE: Using single database connection."
        db.init()

    if options.params is not None:
        td.generate(db.connection, options.params[0], options.params[1], options.params[2])
        if not options.quiet:
            print "DATABASE: Using user provided params to generate test data."

    if options.generate:
        if options.params is None:
            if not options.quiet:
                print "DATABASE: Using default params to generate test data."
            td.generate(db.connection)
        elif not options.quiet:
            print "DATABASE: Using user provided params to generate test data."

    if not options.quiet:
        print "API     : Stalker api listening on {}:{}".format(
            options.host,
            str(options.port)
        )
        print "API     : debug mode = {}".format(options.debug)

    app.run(host=options.host, port=options.port, debug=options.debug)
