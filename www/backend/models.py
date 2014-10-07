""" . """
from mongokit import Document
from datetime import datetime
import config


class Stalker(Document):

    """docstring for Stalker."""

    __database__ = config.DATABASE['name']
    __collection__ = 'stalkers'

    structure = {
        'stalker_id': unicode,
        'relationship_status': unicode,
        'birthdate': unicode,
        'gender': unicode,
        'linkedIn_id': unicode,
        'industry': unicode
    }
    #validators = {
    #    'name': max_length(50),
    #    'email': max_length(120)
    #}

    required_fields = ['stalker_id']
    #default_values = {'creation': datetime.utcnow}
    use_dot_notation = True


class Search(Document):

    """docstring for Search."""

    __database__ = config.DATABASE['name']
    __collection__ = 'searches'

    structure = {
        'stalker_id': unicode,
        'location': {
            'lat': float,
            'long': float
        },
        'victim_id': unicode,
        'creation_time': datetime
    }
    #validators = {
    #    'name': max_length(50),
    #    'email': max_length(120)
    #}

    required_fields = ['stalker_id']
    default_values = {'creation_time': datetime.utcnow}
    use_dot_notation = True


class Victim(Document):

    """docstring for Victim."""

    __database__ = config.DATABASE['name']
    __collection__ = 'victims'

    structure = {
        'victim_id': unicode,
    }
    #validators = {
    #    'name': max_length(50),
    #    'email': max_length(120)
    #}

    required_fields = ['victim_id']
    use_dot_notation = True
