import codecs
import time

from Scraper.Writer.JSONWriter import JSONWriter


# Downloads a list of links to contract pages
# main <pathToFileWithContractLinkPerLine> <FolderWhereContractLinksWillBeDownloaded>
def main(inputFolder: str, outputFolder: str):
    file_with_urls: str = inputFolder
    output_folder: str = outputFolder

    f = codecs.open(file_with_urls, 'r', 'utf-8')
    urls = (("https://www.contratos.gov.co" + line.strip(), output_folder) for line in f)

    for url in urls:
        time.sleep(5)
        writer = JSONWriter(url)
        writer.write()

# main(["data/all_links", "data/contracts/"])
