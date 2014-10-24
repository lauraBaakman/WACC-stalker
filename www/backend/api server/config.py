""" docstring. """
from flask import make_response
from bson.json_util import dumps

DATABASE = {
    'name': 'wacc',
    'host': 'localhost',
    'port':  27017
}


def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    """
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})

    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
