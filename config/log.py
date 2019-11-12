import logging

import uuid


class CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def __init__(self, logger, extra):
        super().__init__(logger, extra)

    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra.get('request_id'), msg), kwargs


class LoggingConfiguration(object):

    logger = None
    adapter = None

    @staticmethod
    def initialize_logger():
        LoggingConfiguration.logger = logging.getLogger(__name__)
        LoggingConfiguration.logger.setLevel(LoggingConfiguration.get_default_log_level())
        LoggingConfiguration.logger.addHandler(LoggingConfiguration.get_default_handler())
        LoggingConfiguration.adapter = CustomAdapter(LoggingConfiguration.logger, {})
        LoggingConfiguration.update_request_id()

    @staticmethod
    def get_default_logger():
        return LoggingConfiguration.adapter

    @staticmethod
    def update_request_id():
        request_id = str(uuid.uuid4())
        LoggingConfiguration.adapter.extra.update({"request_id": request_id})

    @staticmethod
    def get_default_handler():
        handler = logging.StreamHandler()
        handler.setLevel(LoggingConfiguration.get_default_log_level())
        handler.setFormatter(LoggingConfiguration.get_default_log_formatter())
        return handler

    @staticmethod
    def get_default_log_level():
        return logging.INFO

    @staticmethod
    def get_default_log_formatter():
        return logging.Formatter(fmt="[%(asctime)s] %(levelname)s [%(funcName)s:%(lineno)d] %(message)s")
