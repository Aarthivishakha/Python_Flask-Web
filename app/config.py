import os


class Config(object):
    APP_NAME = os.environ.get("APP_NAME", "Flask Web API")
    APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "legacy")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    JSON_SORT_KEYS = False
