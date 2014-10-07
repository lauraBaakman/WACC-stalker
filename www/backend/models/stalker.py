""" . """
from mongokit import Document
#from datetime import datetime
from resources import StalkerResource


class Stalker(Document):

    """docstring for Stalker."""

    test = StalkerResource()

    __database__ = 'wacc'
    __collection__ = 'stalkers'

    structure = {
        'facebook_id': str,
        'relationship_status': str,
        'birthdate': str,
        'gender': str,
        'linkedIn_id': str,
        'industry': str
    }
    #validators = {
    #    'name': max_length(50),
    #    'email': max_length(120)
    #}

    required_fields = ['facebook_id']
    #default_values = {'creation': datetime.utcnow}
    use_dot_notation = True
