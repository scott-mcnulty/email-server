import os


class BaseConfig(object):
    """
    Base application config.
    """

    # Flask
    # http://flask.pocoo.org/docs/config
    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')

    # Flask SQLAlchemy
    # http://flask-sqlalchemy.pocoo.org/config
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:////tmp/myapi.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS',
        False
    )

    # Flask JWT Extended
    # https://flask-jwt-extended.readthedocs.io/en/latest/options.html

    # Flask Caching
    # https://flask-caching.readthedocs.io/en/latest/#configuration-flask-caching
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')

    # Flasgger
    # https://github.com/rochacbruno/flasgger
    SWAGGER = {
        'title': 'Myapi'
    }


class TestConfig(BaseConfig):
    """Used for when we run tests"""

    # Use in memory so database + tables can be recreated and 
    # dropped as a fixture step in pytest
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProdConfig(BaseConfig):
    """Deployment config"""
    
    TESTING = False
