import json
import traceback

from config.log import LoggingConfiguration
from config.settings import settings
from rabbitmq.rmq_consumer import RmqConsumer
from services.product_transformation_result import set_gs_flag

GS_FLAG_RMQ_QUEUE = settings.get("GS_FLAG_RMQ_QUEUE")
GS_FLAG_RMQ_ROUTING_KEY = settings.get("GS_FLAG_RMQ_ROUTING_KEY")
GS_FLAG_RMQ_EXCHANGE = settings.get("GS_FLAG_RMQ_EXCHANGE")


class GsFlagRmqConsumer(RmqConsumer):

    @staticmethod
    def callback(ch, method, properties, body):
        LoggingConfiguration.update_request_id()
        logger = LoggingConfiguration.get_default_logger()
        logger.info("rabbit mq consumer message received: {}".format(body))
        dict_body = json.loads(body)
        try:
            res = set_gs_flag(
                dict_body.get('fixtureId'),
                dict_body.get('price')
            )
        except Exception as e:
            logger.error("MESSAGE PROCESSING FAILED: {}".format(str(e)))
            traceback.print_exc()
            res = False
        return res

    def get_queue_name(self):
        return GS_FLAG_RMQ_QUEUE

    def get_routing_key(self):
        return GS_FLAG_RMQ_ROUTING_KEY

    def get_exchange_name(self):
        return GS_FLAG_RMQ_EXCHANGE
