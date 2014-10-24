""" . """
from mongokit import Connection
from mongokit import ReplicaSetConnection
from models import Stalker, Search, Victim
import config

connection = None


def init(use_replica=False):
    """ . """
    global connection

    if use_replica:
        connection = ReplicaSetConnection(
            host=config.DATABASE_REPLICA['hosts'],
            replicaset=config.DATABASE_REPLICA['replicaset'],
        )
    else:
        connection = Connection(config.DATABASE['host'], config.DATABASE['port'])

    connection.register([Stalker, Search, Victim])

if __name__ == '__main__':
    init()
