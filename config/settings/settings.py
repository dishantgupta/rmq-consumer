import configparser
import os as __os

__env_attrs = __os.environ
env = __env_attrs.get('ENV')

if not env:
    env = "dev"

config = configparser.ConfigParser()

if env == "dev":
    config.read('config/settings/dev.ini')
elif env == "qa":
    config.read('config/settings/qa.ini')
elif env == "stage":
    config.read('config/settings/stage.ini')
elif env == "prod":
    config.read('config/settings/prod.ini')
elif env == "local":
    config.read('config/settings/local.ini')


def get(key):
    value = config.get('DEFAULT', key)
    if not value:
        value = __env_attrs.get(key) or ''
    return value


def getall():
    return config

