""" . """
from mongokit import Connection

global connection

def init(db_host, db_port):
    """ . """
    global connection
    connection = Connection(db_host, db_port)
