from abc import ABC, abstractmethod, abstractproperty
from flaskext.mysql import MySQL
import pymysql

class IConnectionData(ABC):
    """
    abstract class for getting mysql connection
    """

    @property
    @abstractproperty
    def user_name(self):
        pass

    @property
    @abstractproperty
    def password(self):
        pass

    @property
    @abstractproperty
    def db_name(self):
        pass

    @property
    @abstractproperty
    def db_host(self):
        pass


class ConnectionData(IConnectionData):
    """
    has connection strings and has getters for them
    """

    def __init__(self):
        self._user_name = "darts"
        self._password = "darts2017"
        self._db_name = "hmis"
        self._db_host = "karduni.ccvkgysiex9c.us-west-2.rds.amazonaws.com"

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def db_name(self):
        return self._db_name

    @property
    def db_host(self):
        return self._db_host

class ConnectionUtility():

    @staticmethod
    def getConnection(connection_data):

        connection = pymysql.connect(
            host=connection_data.db_host,
            user=connection_data.user_name,
            password=connection_data.password,
            db=connection_data.db_name,
            autocommit=True
        )

        return connection


