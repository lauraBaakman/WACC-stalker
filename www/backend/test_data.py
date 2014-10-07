""" Test Data. """


def populate(connection):
    """ . """
    stalker = connection.Stalker()
    stalker.stalker_id = u'0001'
    stalker.relationship_status = u'single'
    stalker.birthdate = u'23-03-1990'
    stalker.gender = u'female'
    stalker.linkedIn_id = u'L0001'
    stalker.industry = u'computing science'
    stalker.save()

    stalker = connection.Stalker()
    stalker.stalker_id = u'0002'
    stalker.relationship_status = u'not single'
    stalker.birthdate = u'23-03-1996'
    stalker.gender = u'male'
    stalker.linkedIn_id = u'L0002'
    stalker.industry = u'computing science'
    stalker.save()

    search = connection.Search()
    search.stalker_id = u'0001'
    search.location.lat = 52.6888
    search.location.long = 50.6668
    search.save()

    search = connection.Search()
    search.stalker_id = u'0002'
    search.location.lat = 60.6888
    search.location.long = 30.6668
    search.victim_id = u'0001'
    search.save()

    victim = connection.Victim()
    victim.victim_id = u'0001'
    victim.save()


def clear(connection):
    """ Clear database. """
    connection.wacc.drop_collection('stalkers')
    connection.wacc.drop_collection('searches')
    connection.wacc.drop_collection('victims')
