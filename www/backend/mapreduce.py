"""Test map reduce."""
import database as db
from bson import Code

from models import Stalker, Search, Victim


def fillDB():
    """."""
    stalker1 = db.connection.Stalker()
    stalker1.stalker_id = u'stalker1'
    stalker1.relationship_status = u'single'
    stalker1.save()
    stalker2 = db.connection.Stalker()
    stalker2.stalker_id = u'stalker2'
    stalker2.relationship_status = u'married'
    stalker2.save()
    stalker3 = db.connection.Stalker()
    stalker3.stalker_id = u'stalker3'
    stalker3.relationship_status = u'widowed'
    stalker3.save()
    stalker4 = db.connection.Stalker()
    stalker4.stalker_id = u'stalker4'
    stalker4.relationship_status = u'single'
    stalker4.save()

    search1 = db.connection.Search()
    search1.stalker_id = u'stalker1'
    search1.location['country_code'] = u'BE'
    search1.save()
    search2 = db.connection.Search()
    search2.stalker_id = u'stalker1'
    search2.location['country_code'] = u'NL'
    search2.victim_id = u'victim1'
    search2.save()
    search3 = db.connection.Search()
    search3.stalker_id = u'stalker1'
    search3.victim_id = u'victim2'
    search3.location['country_code'] = u'LUX'
    search3.save()
    search4 = db.connection.Search()
    search4.stalker_id = u'stalker3'
    search4.location['country_code'] = u'NL'
    search4.victim_id = u'victim3'
    search4.save()

    victim1 = db.connection.Victim()
    victim1.victim_id = u'victim1'
    victim1.save()
    victim2 = db.connection.Victim()
    victim2.victim_id = u'victim2'
    victim2.save()
    victim3 = db.connection.Victim()
    victim3.victim_id = u'victim3'
    victim3.save()


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

    fillDB()
    stalker_relationship_frequency()
    search_location_frequency()
