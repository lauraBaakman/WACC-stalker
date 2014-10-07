""" Test Data. """


def populate(connection):
    """ . """
    stalker = connection.Stalker()
    stalker.stalker_id = '0001'
    stalker.relationship_status = 'single'
    stalker.birthdate = '23-03-1990'
    stalker.gender = 'female'
    stalker.linkedIn_id = 'L0001'
    stalker.industry = 'computing science'
    stalker.save()

    stalker = connection.Stalker()
    stalker.stalker_id = '0002'
    stalker.relationship_status = 'not single'
    stalker.birthdate = '23-03-1996'
    stalker.gender = 'male'
    stalker.linkedIn_id = 'L0002'
    stalker.industry = 'computing science'
    stalker.save()

    search = connection.Search()
    search.stalker_id = '0001'
    search.location.lat = 52.6888
    search.location.long = 50.6668
    search.save()

    search = connection.Search()
    search.stalker_id = '0002'
    search.location.lat = 60.6888
    search.location.long = 30.6668
    search.victim_id = '0001'
    search.save()

    victim = connection.Victim()
    victim.victim_id = '0001'
    victim.save()


def clear(connection):
    """ Clear database. """
    connection.wacc.drop_collection('stalkers')
    connection.wacc.drop_collection('searches')
    connection.wacc.drop_collection('victims')
