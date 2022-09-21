import codecs

import requests


class UrlExtractor:

    def __init__(self, base_url, pagina, objeto, cuantia, output_folder):
        self.url = base_url
        self.current_pagina = pagina
        self.objeto = objeto
        self.cuantia = cuantia
        self.output_folder = output_folder

    def get_url(self):
        return self.url.format(pagina=str(self.current_pagina), cuantia=self.cuantia, objeto=self.objeto)

    def extract(self):
        try:
            response = requests.get(self.get_url())
            if (response.status_code == 200):
                if not "No existen resultados que cumplan con los" in response.text:
                    return response.text
            return ""
        except Exception:
            print("error while grabbing.." + self.get_url())
            return ""

    def extract_all(self):
        html_content = ""
        while True:
            html_content = self.extract()
            if html_content == "":
                break
            filename = self.output_folder + "/{objeto}_{cuantia}_{pagina}".format(objeto=self.objeto,
                                                                                  cuantia=self.cuantia,
                                                                                  pagina=self.current_pagina)
            print("saving.." + filename)
            f = codecs.open(filename, 'w', 'utf-8')
            f.write(html_content)
            f.close()
            self.current_pagina = self.current_pagina + 1
