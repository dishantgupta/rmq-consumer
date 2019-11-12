from config.settings import settings
from db.mysql_connector import MySqlConnector


MYSQL_HOST = settings.get("MYSQL_HOST")
CC_MYSQL_PORT = settings.get("CC_MYSQL_PORT")
MYSQL_USER = settings.get("MYSQL_USER")
MYSQL_PASS = settings.get("MYSQL_PASS")
CC_MYSQL_DATABASE = settings.get("CC_MYSQL_DATABASE")
CC_MYSQL_DIALECT = settings.get("CC_MYSQL_DIALECT")


class CCMySqlConnector(object):

    engine = None

    def __init__(self):
        self.engine = MySqlConnector.get_engine(
            MYSQL_HOST, CC_MYSQL_PORT, CC_MYSQL_DATABASE, MYSQL_USER,
            MYSQL_PASS, CC_MYSQL_DIALECT)

    def execute(self, query):
        return MySqlConnector.execute_request(self.engine, query)
