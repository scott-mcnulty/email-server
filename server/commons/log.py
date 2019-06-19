import logging
import sys


# Straps our logging to the gunicorn logger
logger = logging.getLogger('gunicorn.error')


def log(message, level='info'):
    """Log a message to the logger using a specified logging level."""

    level_mapping = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if level not in level_mapping:
        level = 'info'
        level_mapping.get('warning')(
            'Bad logging level supplied to utils.log. '
            'Use one of the following: {}'.format(level_mapping.keys())
        )

    level_mapping.get(level)(message)