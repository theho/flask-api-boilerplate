from flask_jwt import JWT
from .models import User


def authenticate(username, password):
    user = User.query.filter(User.username == username).scalar()

    if user and user.check_password(password):
        return user


def identify(payload):
    return User.query.filter(User.id == payload['identity']).scalar()


def init_app(app):
    jwt = JWT(app, authenticate, identify)

    # jwt.jwt_payload_handler(make_payload)
