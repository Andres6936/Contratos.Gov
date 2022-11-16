import json
from pathlib import Path
from typing import Tuple

import requests
from requests import Response

from Scraper.Config.Configuration import Configuration
from Scraper.Directory import Directory
from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.Writer.IWriter import IWriter
from Scraper.contract import ContractParser


class JSONWriter(IWriter):
    __configuration = Configuration()

    def __init__(self, contract: Tuple[str, str]):
        (url, output_folder) = contract
        self.url: str = url
        self.outputFolder: str = output_folder

    def GetOutputFolder(self) -> str:
        return self.__configuration.GetOutputFolder()

    def write(self):
        try:
            result: Response = requests.get(self.url)
            if result.status_code == 200:
                folder: Path = self.GetOutputFolder() / Path(self.url.split("=")[1].replace("/", "_") + ".json")
                Directory.CreateFileIfNotExist(folder.parent)
                GeneralMessage.publish("The name of file to write is: " + folder.as_posix())
                with folder.open(mode='a+', encoding='utf-8') as f:
                    contract = ContractParser(result.text).parse()
                    f.write(json.dumps(contract) + "\n")
                    f.close()
            else:
                GeneralMessage.publishError("error downloading.." + self.url)
        except Exception as e:
            GeneralMessage.publishError(e)
            GeneralMessage.publishError("error downloading.." + self.url)
