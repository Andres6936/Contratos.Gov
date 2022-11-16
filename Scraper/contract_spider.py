import codecs
import time

from Scraper.Config.Configuration import Configuration
from Scraper.Writer.IWriter import IWriter
from Scraper.Writer.JSONWriter import JSONWriter


# Downloads a list of links to contract pages
# main <pathToFileWithContractLinkPerLine> <FolderWhereContractLinksWillBeDownloaded>
def main():
    f = codecs.open(Configuration().GetInputFolder(), 'r', 'utf-8')
    urls = (("https://www.contratos.gov.co" + line.strip()) for line in f)

    for url in urls:
        time.sleep(5)
        writer: IWriter = JSONWriter(url)
        writer.write()

# main(["data/all_links", "data/contracts/"])
