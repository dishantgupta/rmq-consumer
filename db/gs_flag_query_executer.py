import json

from config.log import LoggingConfiguration
from db.cc_mysql_connector import CCMySqlConnector
from config.settings import settings


ABC_GS_FLAG_TABLE = settings.get('ABC_GS_FLAG_TABLE')


class GsFlagQueryExecutor(object):

    @staticmethod
    def get_flag(fixture_id=None):
        query = None
        where_clause = None
        flag = None
        cc_mysql_connector = CCMySqlConnector()
        logger = LoggingConfiguration.get_default_logger()

        # processing
        if fixture_id:
            where_clause = "fixture_id={}".format(fixture_id)
        if where_clause:
            query = "select gs_flag from {} where {} order by timestamp desc limit 1".format(ABC_GS_FLAG_TABLE, where_clause)
            res = cc_mysql_connector.execute(query)
            flag = res.first()
            if flag:
                flag = flag[0]

        logger.info("mysql query: {} result: {}".format(query, flag))
        return flag

    @staticmethod
    def set_flag(flag, fixture_data):
        logger = LoggingConfiguration.get_default_logger()
        cc_mysql_connector = CCMySqlConnector()
        if fixture_data:
            fixture_id = fixture_data.pop("fixture_id")
            query = "insert into {} (fixture_id, gs_flag, extra_data) values ('{}', '{}', '{}')".format(
                ABC_GS_FLAG_TABLE, fixture_id, int(flag), json.dumps(fixture_data))
            res = cc_mysql_connector.execute(query)
            logger.info("mysql query: {} result: {}".format(query, res))
            return True
        return False
