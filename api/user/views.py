from flask import current_app
from flask_classful import route
from .models import User
from .schemas import signup_schema
from webargs.flaskparser import use_args

from ..common import APIView


class UsersView(APIView):
    route_base = '/v1/users'

    @route('signup', methods=['POST'])
    @use_args(signup_schema)
    def signup(self, args):
        u = User.create(**args)
        token = generate_token(u)
        return {'token': token.decode('utf-8')}, 201
        # return token, 201


def generate_token(user):
    """ Currently this is workaround
    since the latest version that already has this function
    is not published on PyPI yet and we don't want
    to install the package directly from GitHub.
    See: https://github.com/mattupstate/flask-jwt/blob/9f4f3bc8dce9da5dd8a567dfada0854e0cf656ae/flask_jwt/__init__.py#L145
    Hope it will be released on PyPI soon.
    https://github.com/mattupstate/flask-jwt/issues/38#issuecomment-127167806
    """
    _jwt = current_app.extensions['jwt']
    token = _jwt.jwt_encode_callback(user)
    return token
