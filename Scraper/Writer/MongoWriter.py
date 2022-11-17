from pymongo import MongoClient

from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.Writer.IWriter import IWriter


class MongoWriter(IWriter):
    _database = MongoClient().Contra

    def write(self):
        collection = self._database.Contracts
        collection.insert_one(self.parser.parser())
        GeneralMessage.publish("Element inserted")
