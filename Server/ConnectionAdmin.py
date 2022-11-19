import os
import urllib.parse

from pymongo import MongoClient


class ConnectionAdmin:
    _instance = None
    _client: MongoClient = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConnectionAdmin, cls).__new__(cls)
            cls._client = MongoClient(
                f"mongodb://{cls.GetUsernameAdmin()}"
                f":{cls.GetUsernamePassword()}"
                f"@{cls.GetDatabaseURL()}"
                f":{cls.GetDatabasePort()}")
        return cls._instance

    @staticmethod
    def GetUsernameAdmin():
        username = os.environ["MONGO_USERNAME_ADMIN"]
        return urllib.parse.quote_plus(username)

    @staticmethod
    def GetUsernamePassword():
        password = os.environ["MONGO_PASSWORD_ADMIN"]
        return urllib.parse.quote_plus(password)

    @staticmethod
    def GetDatabaseURL():
        return os.environ["MONGO_DATABASE_URL"]

    @staticmethod
    def GetDatabasePort():
        return os.environ["MONGO_DATABASE_PORT"]

    @staticmethod
    def GetCollection(cls, collection):
        return cls._client[collection]
