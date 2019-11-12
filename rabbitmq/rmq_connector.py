
import pika
from config.settings import settings


AMQP_HOST = settings.get("AMQP_HOST")
AMQP_VHOST = settings.get("AMQP_VHOST")
RABBITMQ_PORT = settings.get("RABBITMQ_PORT")
AMQP_USER = settings.get("AMQP_USER")
AMQP_PASS = settings.get("AMQP_PASS")


def get_rmq_connection():
    credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=AMQP_HOST,
            port=RABBITMQ_PORT,
            virtual_host=AMQP_VHOST,
            credentials=credentials
        )
    )
    return connection
