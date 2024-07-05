"""
File with valid data for users and passwords for the site "https://www.saucedemo.com/"
"""

import random
import logging


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")
logger = logging.getLogger(__name__)

valid_names = [
    'standard_user',
    'locked_out_user', # invalid user
    'problem_user',
    'performance_glitch_user',
    'error_user',
    'visual_user'
]

valid_passwords = [
    'secret_sauce'
]


def get_valid_name():
    if valid_names == 'locked_out_user':
        logger.info(f'Exs(ValueError): Username is invalid')
        raise ValueError('Username is invalid')
    logger.info(f'Username -> is valid')
    return random.choice(valid_names)


