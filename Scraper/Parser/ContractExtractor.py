from pathlib import Path

import requests
from requests import Response

from Scraper.IO.Directory import Directory
from Scraper.Logger.GeneralMessage import GeneralMessage


class ContractExtractor:
    def __init__(self, base_url: str, pagina: int, objeto: str, cuantia: str, output_folder: str):
        self.url = base_url
        self.current_pagina = pagina
        self.objeto = objeto
        self.cuantia = cuantia
        self.output_folder = output_folder

    def get_url(self):
        return self.url.format(pagina=str(self.current_pagina), cuantia=self.cuantia, objeto=self.objeto)

    def extract(self) -> str:
        try:
            response: Response = requests.get(self.get_url())
            if response.status_code == 200:
                if not "No existen resultados que cumplan con los" in response.text:
                    return response.text
            return ""
        except Exception:
            print("error while grabbing.." + self.get_url())
            return ""

    def GetNameFile(self) -> str:
        return f"{self.objeto}_{self.cuantia}_{self.current_pagina}.html"

    def extract_all(self):
        while True:
            GeneralMessage.publish("Start new cycle")
            html_content = self.extract()
            if html_content == "":
                break
            filename = Path(self.output_folder, self.GetNameFile())
            GeneralMessage.publish("The name of file to write is: " + filename.as_posix())
            Directory.CreateFileIfNotExist(filename.parent)
            with filename.open(mode='a+', encoding='utf-8') as f:
                f.write(html_content)
                f.close()
                self.current_pagina = self.current_pagina + 1
