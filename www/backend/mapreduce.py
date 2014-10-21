"""Test map reduce."""
import database as db
from bson import Code
from bson.son import SON

from models import Stalker, Search, Victim


def stalker_relationship_frequency():
    """Method to get the frquency of relationship status of stalkers."""
    map = Code(open('./maps/relationship_frequency.js', 'r').read())
    reduce = Code(open('./reduces/frequency.js', 'r').read())
    result = db.connection.wacc.stalkers.map_reduce(
        map, reduce
    )
    return result


def search_location_frequency():
    """Method to get the frquency of locations of searches."""
    map = Code(open('./maps/location_frequency.js', 'r').read())
    reduce = Code(open('./reduces/frequency.js', 'r').read())
    result = db.connection.wacc.searches.map_reduce(
        map, reduce
    )
    return result


def gender_location_frequency():
    """ Method to stalker info about searches. """
    map = Code(open('./maps/stalker_info.js', 'r').read())
    reduce = Code(open('./reduces/stalker_info.js', 'r').read())
    result = db.connection.wacc.stalkers.map_reduce(
        map, reduce, "stalker_info"
    )

    map = Code(open('./maps/search_info.js', 'r').read())
    reduce = Code(open('./reduces/search_info.js', 'r').read())
    result = db.connection.wacc.searches.map_reduce(
        map, reduce, out=SON([("reduce", "stalker_info")])
    )
    # Now if the key already exist the reduce function is used to merge the results.
    return result


def gender_relationship_frequency():
    """ . """
    map = Code(open('./maps/gender_relationship_frequency.js', 'r').read())
    reduce = Code(open('./reduces/frequency.js', 'r').read())
    result = db.connection.wacc.stalkers.map_reduce(
        map, reduce, "tmp"
    )
    return result

if __name__ == '__main__':
    db.init()
    db.connection.register([Stalker, Search, Victim])

    #db.connection.wacc.drop_collection('stalkers')
    #db.connection.wacc.drop_collection('searches')
    #db.connection.wacc.drop_collection('victims')

    #stalker_relationship_frequency()
    #search_location_frequency()
    # gender_location_frequency()
    gender_relationship_frequency()
