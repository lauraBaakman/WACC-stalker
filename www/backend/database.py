""" . """
from mongokit import Connection
import config

def init():
    """ . """
    return Connection(config.DATABASE['host'], config.DATABASE['port'])
