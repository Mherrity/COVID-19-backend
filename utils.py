import json
from flask import make_response
def dict_response(JSON):
    return make_response(json.dumps(JSON))
