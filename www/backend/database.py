""" . """
from mongokit import Connection
import config

global connection


def init():
    """ . """
    global connection
    connection = Connection(config.DATABASE['host'], config.DATABASE['port'])
