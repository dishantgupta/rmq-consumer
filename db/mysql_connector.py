import abc

from sqlalchemy import create_engine


class MySqlConnector(abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def get_engine(host, port, database,  username, password, dialect):
        engine = create_engine("{db_type}://{username}:{password}@{host}:{port}/{db}".format(
            db_type=dialect, username=username, password=password, host=host, port=port, db=database), echo='debug'
        )
        return engine

    @staticmethod
    def execute_request(engine, query):
        connection = engine.connect()
        result = connection.execute(query)
        return result
