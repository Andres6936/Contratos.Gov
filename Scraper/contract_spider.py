import codecs
import json
import time
from multiprocessing import Value
from pathlib import Path
from typing import Tuple

import requests
from requests import Response

from Scraper.GeneralMessage import GeneralMessage
from Scraper.contract import ContractParser

counter = Value('i', 1)


def ExtractContractInformation(pair: Tuple[str, str]):
    time.sleep(5)
    url = pair[0]
    global counter
    output_folder = Path(pair[1])
    try:
        result: Response = requests.get(url)
        if result.status_code == 200:
            temporalFolder = counter.value % 400
            folder: Path = output_folder / Path(str(temporalFolder), url.split("=")[1].replace("/", "_") + ".json")
            GeneralMessage.publish("The name of file to write is: " + folder.as_posix())
            with folder.open(mode='a+', encoding='utf-8') as f:
                contract = ContractParser(result.text).parse()
                f.write(json.dumps(contract) + "\n")
                f.close()
        # print("downloaded.." + url)
        else:
            GeneralMessage.publishError("error downloading.." + url)
    except Exception as e:
        GeneralMessage.publishError(e)
        GeneralMessage.publishError("error downloading.." + url)
    counter.value += 1
    GeneralMessage.publish("done.." + str(counter.value))


# Downloads a list of links to contract pages
# main <pathToFileWithContractLinkPerLine> <FolderWhereContractLinksWillBeDownloaded>
def main(inputFolder: str, outputFolder: str):
    file_with_urls: str = inputFolder
    output_folder: str = outputFolder

    for i in range(0, 400):
        folder: Path = Path(output_folder, str(i))
        if not folder.exists():
            folder.mkdir()

    f = codecs.open(file_with_urls, 'r', 'utf-8')
    urls = (("https://www.contratos.gov.co" + line.strip(), output_folder) for line in f)

    for url in urls:
        ExtractContractInformation(url)

# main(["data/all_links", "data/contracts/"])
