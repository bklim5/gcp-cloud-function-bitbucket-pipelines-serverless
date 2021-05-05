from importlib import import_module
from os import environ

environment_name = environ.get('ENVIRONMENT_NAME', 'dev')
config = import_module('app.config.{}'.format(environment_name)).CONFIG


def get_config():
    return config
