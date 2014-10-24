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

    required_fields = ['stalker_id', 'birthdate', 'gender']
    use_dot_notation = True


class Search(Document):

    """docstring for Search."""

    __database__ = config.DATABASE['name']
    __collection__ = 'searches'

    structure = {
        'stalker_id': unicode,
        'location': {
            'lat': float,
            'long': float,
            'country_code': unicode
        },
        'victim_id': unicode,
        'creation_time': datetime
    }

    required_fields = ['stalker_id', 'location.lat', 'location.long', 'location.country_code']
    default_values = {'creation_time': datetime.utcnow}
    use_dot_notation = True


class Victim(Document):

    """docstring for Victim."""

    __database__ = config.DATABASE['name']
    __collection__ = 'victims'

    structure = {
        'victim_id': unicode,
    }

    required_fields = ['victim_id']
    use_dot_notation = True
