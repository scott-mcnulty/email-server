"""
http://docs.gunicorn.org/en/stable/settings.html
"""
import os


bind = ':{}'.format(os.environ.get('PORT', 8000))
workers = int(os.environ.get('PROCESSES', 1))
threads = int(os.environ.get('THREADS', 1))

# http://docs.gunicorn.org/en/stable/settings.html#loglevel
loglevel = os.environ.get('LOG_LEVEL', 'debug')