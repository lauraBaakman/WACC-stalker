"""Test map reduce."""
import database as db
from bson import Code

from models import Stalker, Search, Victim

def stalker_relationship_frequency():
    """Method to get the frquency of relationship status of stalkers."""
    map = Code(open('./maps/relationship_frequency.js', 'r').read())
    reduce = Code(open('./reduces/frequency.js', 'r').read())
    result = db.connection.wacc.stalkers.map_reduce(map, reduce, "myresults")
    return result


def search_location_frequency():
    """Method to get the frquency of locations of searches."""
    map = Code(open('./maps/location_frequency.js', 'r').read())
    reduce = Code(open('./reduces/frequency.js', 'r').read())
    result = db.connection.wacc.searches.map_reduce(map, reduce, "myresults")
    return result


if __name__ == '__main__':
    db.init()
    db.connection.register([Stalker, Search, Victim])
    db.connection.wacc.drop_collection('stalkers')
    db.connection.wacc.drop_collection('searches')
    db.connection.wacc.drop_collection('victims')

    stalker_relationship_frequency()
    search_location_frequency()
