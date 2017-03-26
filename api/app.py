# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask

from api import commands, user
from api.extensions import bcrypt, db, migrate
from api.settings import ProdConfig
from api.user import jwt_extension

# Views
from api.dummy.view import DummyView
from api.user.views import UsersView


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_views(app)
    # register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    db.init_app(app)
    jwt_extension.init_app(app)
    migrate.init_app(app, db)
    return None


def register_views(app):
    """Register Flask blueprints."""
    DummyView.register(app)
    UsersView.register(app)

    return None


# def register_errorhandlers(app):
#     """Register error handlers."""
#     def render_error(error):
#         """Render error template."""
#         # If a HTTPException, pull the `code` attribute; default to 500
#         error_code = getattr(error, 'code', 500)
#         return render_template('{0}.html'.format(error_code)), error_code
#     for errcode in [401, 404, 500]:
#         app.errorhandler(errcode)(render_error)
#     return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
