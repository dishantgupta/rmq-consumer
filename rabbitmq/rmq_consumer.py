import abc

from config.log import LoggingConfiguration
from rabbitmq.rmq_connector import get_rmq_connection


class RmqConsumer(abc.ABC):

    _connection = None
    _channel = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init()

    def get_connection(self):
        return self._connection

    def get_queue_type(self):
        return "direct"

    def get_durable(self):
        return True

    def get_auto_delete(self):
        return False

    def get_auto_ack(self):
        return True

    def _init(self):
        self._connection = get_rmq_connection()
        self._channel = self._connection.channel()
        self._declare_queue()
        self._bind_queue()

    def _bind_queue(self):
        self._channel.queue_bind(
            self.get_queue_name(),
            self.get_exchange_name(),
            self.get_routing_key()
        )

    def _declare_queue(self):
        self._channel.queue_declare(self.get_queue_name())

    def consume(self):
        logger = LoggingConfiguration.get_default_logger()
        self._channel.basic_consume(
            self.get_queue_name(),
            self.callback,
            self.get_auto_ack()
        )
        # start consuming, handle and log error, close connection
        self._channel.start_consuming()

    def get_error_message(self, exception):
        return "rabbit mq consumer processing failed, error is: {}".format(str(exception))

    @abc.abstractmethod
    def get_queue_name(self):
        pass

    @abc.abstractmethod
    def get_routing_key(self):
        pass

    @abc.abstractmethod
    def get_exchange_name(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def callback(ch, method, properties, body):
        pass
