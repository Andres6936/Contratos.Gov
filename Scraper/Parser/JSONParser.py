from typing import Union

import requests
from requests import Response

from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.contract import ContractParser

JSON = dict[str, Union[list, str, int, float]]


class JSONParser:
    def __init__(self, url: str):
        self.url: str = url

    def parser(self) -> Union[JSON, None]:
        try:
            result: Response = requests.get(self.url)
            if result.status_code == 200:
                return ContractParser(result.text).parse()
            else:
                GeneralMessage.publishError("error downloading.." + self.url)
                return None
        except Exception as e:
            GeneralMessage.publishError(e)
            GeneralMessage.publishError("error downloading.." + self.url)
            return None
