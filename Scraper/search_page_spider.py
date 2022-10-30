from Scraper.UrlExtractor import UrlExtractor


class Contratos:

    def __init__(self, output_folder: str):
        self.url: str = "https://www.contratos.gov.co/consultas/resultadosConsulta.do?&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidRedir=&departamento=&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&objeto={objeto}&paginaObjetivo={pagina}&cuantia={cuantia}&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&fechaInicial=&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&fechaFinal=&desdeFomulario=true&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&tipoProceso=&registrosXPagina=10&numeroProceso=&municipio=0&estado=0&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1"
        self.output_folder: str = output_folder

    def generate_base_urls(self) -> list[UrlExtractor]:
        cuantias: list[str] = ["1", "2", "3", "4", "5"]
        objetos: list[str] = ["10000000", "11000000", "12000000", "15000000", "13000000", "14000000", "27000000",
                              "20000000",
                              "21000000",
                              "22000000", "26000000", "23000000", "24000000", "25000000", "40000000", "32000000",
                              "31000000",
                              "30000000"
                              "39000000", "41000000", "50000000", "52000000", "43000000", "42000000", "44000000",
                              "46000000",
                              "45000000"
                              "47000000", "49000000", "60000000", "48000000", "51000000", "56000000", "54000000",
                              "55000000",
                              "53000000",
                              "94000000", "81000000", "82000000", "86000000", "84000000", "77000000", "91000000",
                              "93000000",
                              "83000000",
                              "70000000", "92000000", "72000000", "80000000", "76000000", "71000000", "73000000",
                              "85000000",
                              "78000000",
                              "90000000", "95000000"]

        extractors: list[UrlExtractor] = list()

        for cuantia in cuantias:
            for objeto in objetos:
                extractors.append(UrlExtractor(self.url, 1, objeto, cuantia, self.output_folder))

        return extractors


def worker(extractor: UrlExtractor):
    extractor.extract_all()


# Download all the results pages containing links to contract pages	
def main(outputFolder: str):
    extractors: list[UrlExtractor] = Contratos(outputFolder).generate_base_urls()

    for extractor in extractors:
        extractor.extract_all()

# uso [PathToOutputFolder]
# main(["/Users/dav009/source/Scraper/pages"])
