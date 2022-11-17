from abc import ABC, abstractmethod

from Scraper.Parser.JSONParser import JSONParser


class IWriter(ABC):
    def __init__(self, parser: JSONParser):
        self.parser: JSONParser = parser

    @abstractmethod
    def write(self):
        return NotImplemented
