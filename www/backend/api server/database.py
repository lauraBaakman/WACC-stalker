""" . """
from mongokit import Connection
from mongokit import ReplicaSetConnection
from models import Stalker, Search, Victim
import config

global connection


def init(use_replica=False):
    """ . """
    global connection

    if not use_replica:
        connection = Connection(config.DATABASE['host'], config.DATABASE['port'])
    else:
        connection = ReplicaSetConnection(
            host="localhost:27017,localhost:27018, localhost:27019",
            replicaset="rs_wacc"
            #read_preferences=pymongo.read_preferences.ReadPreferance.SECONDARY_PREFERRED
        )
    connection.register([Stalker, Search, Victim])
