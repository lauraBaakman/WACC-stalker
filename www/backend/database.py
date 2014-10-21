""" . """
from mongokit import Connection
from mongokit import ReplicaSetConnection
#import pymongo
import config

global connection


def init():
    """ . """
    global connection
    connection = Connection(config.DATABASE['host'], config.DATABASE['port'])


def init_replicas():
    """ Initialization of the replica set connection. """
    global connection
    connection = ReplicaSetConnection(
        host="localhost:27017,localhost:27018, localhost:27019",
        replicaset="rs_wacc"
        #read_preferences=pymongo.read_preferences.ReadPreferance.SECONDARY_PREFERRED
    )
