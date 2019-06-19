import os

from flask import Flask

from server import api, config
from server.extensions import jwt, cors, cache
from server.api import api
from server.commons.log import log


def create_app():

    app = Flask('metro-transit-time-email-server')

    log('Using base config: {}'.format(config.BaseConfig.__dict__), 'debug')
    prod = os.environ.get('PROD')
    if not prod:
        _config = config.TestConfig
    else:
        _config = config.ProdConfig
    app.config.from_object(_config)
    log('Set app config using `{}` with values: {}'.format(_config.__name__, _config.__dict__), 'debug')

    register_extensions(app, prod)
    return app


def register_extensions(app, testing=False):

    jwt.init_app(app)
    cors.init_app(app)
    cache.init_app(app)
    api.init_app(app)
