import json

from flask import make_response
from flask_classful import FlaskView


def output_json(data, code, headers=None):
    content_type = 'application/json'
    dumped = json.dumps(data)
    headers = headers or {}
    headers.update({'Content-Type': content_type})
    response = make_response(dumped, code, headers)
    return response


class APIView(FlaskView):
    representations = {'application/json': output_json}
