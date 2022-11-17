from typing import Union

import requests
from requests import Response

from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.Parser.ContractParser import ContractParser

JSON = dict[str, Union[list, str, int, float]]


class JSONParser:
    def __init__(self, url: str):
        self.url: str = url

    def name(self):
        return self.url.split("=")[1].replace("/", "_") + ".json"

    def parser(self) -> Union[JSON, None]:
        try:
            result: Response = requests.get(self.url)
            if result.status_code == 200:
                return ContractParser(result.text).parse()
            else:
                GeneralMessage.publishError(f"Error Downloading HTML {self.url}, the status is {result.status_code}")
                return None
        except Exception as e:
            GeneralMessage.publishError(f"An exception has occurred {e}, the url is {self.url}")
            return None
