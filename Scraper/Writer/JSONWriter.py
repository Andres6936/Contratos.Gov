import json
from pathlib import Path

from Scraper.Config.Configuration import Configuration
from Scraper.Directory import Directory
from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.Parser.JSONParser import JSONParser
from Scraper.Writer.IWriter import IWriter


class JSONWriter(IWriter):
    __configuration = Configuration()

    def __init__(self, parser: JSONParser):
        self.parser: JSONParser = parser

    def GetOutputFolder(self) -> str:
        return self.__configuration.GetOutputFolder()

    def write(self) -> None:
        folder: Path = self.GetOutputFolder() / Path(self.parser.name())
        Directory.CreateFileIfNotExist(folder.parent)
        GeneralMessage.publish("The name of file to write is: " + folder.as_posix())
        with folder.open(mode='a+', encoding='utf-8') as f:
            contract = self.parser.parser()
            f.write(json.dumps(contract) + "\n")
            f.close()
