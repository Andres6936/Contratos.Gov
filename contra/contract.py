import codecs
import json
import multiprocessing
import string
from multiprocessing import Value
from os import listdir
from typing import Tuple

from lxml import html
from lxml.cssselect import CSSSelector
from unidecode import unidecode

counter = Value('i', 0)


def GetFieldName(value: str) -> str:
    """
    It often happens that you have text data in Unicode, but you need
    to represent it in ASCII. For example when integrating with
    legacy code that does not support Unicode, or for ease of entry
    of non-Roman names on a US keyboard, or when constructing ASCII
    machine identifiers from human-readable Unicode strings that
    should still be somewhat intelligible. A popular example of this
    is when making a URL slug from an article title.

    :param value: The value of field name, generally this not is formatted
    :return: The name of a field for will be used for JSON field
    """
    formatted = unidecode(value.strip()) \
        .replace(" del ", " ") \
        .replace(" de ", " ") \
        .replace(" al ", " ") \
        .replace(" y ", " ") \
        .replace(" a ", " ")

    # Capitalize each word before of remove the whitespaces
    return string.capwords(formatted).replace(" ", "")


# Extracts fields from contract pages:
# i.e: https://www.contratos.gov.co/consultas/detalleProceso.do?numConstancia=15-11-4035910
def extract_field(list_of_tds) -> Tuple[str, str]:
    field_name = ""
    field_value = ""
    for td_tag in list_of_tds:
        if td_tag.get("class") == "tablaslistOdd":
            if field_value != "":
                field_name = field_value
            field_value = td_tag.text_content().strip()

        if td_tag.get("class") == "tablaslistEven":
            field_name = td_tag.text_content().strip()

    return GetFieldName(field_name), field_value


def extract_doc(list_of_tds):
    def GetNameContract(td_tag) -> Tuple[str, str]:
        matches = td_tag.find('a')
        if matches is not None:
            return matches.text, matches.get('href')
        return "", ""

    (name, url) = GetNameContract(list_of_tds[0])
    description = list_of_tds[1].text_content().strip()
    publication_date = list_of_tds[5].text_content().strip()

    # Making sure we don't extract the header of the table
    if name != "" and name != "Nombre":
        return {
            "Name": name,
            "Url": url,
            "Description": description,
            "PublicationDate": publication_date
        }
    return None


class ContractParser:

    def __init__(self, html_content: str):
        self.parsed_content = html.fromstring(html_content)

    def parse(self):
        contract_representation = dict()
        contract_representation['documents'] = list()

        tr_tags = CSSSelector("tr")(self.parsed_content)
        for tr_tag in tr_tags:

            td_tags = CSSSelector("td")(tr_tag)

            # it is a field : field value
            if len(td_tags) == 2:
                field_name, field_value = extract_field(td_tags)
                if field_name and field_value:
                    contract_representation[field_name] = field_value

            # it is one of the linked docs
            if len(td_tags) == 6:
                document = extract_doc(td_tags)
                if document:
                    contract_representation['documents'].append(document)
        return contract_representation


def parse_contract_page(page_file):
    f = codecs.open(page_file, 'r', 'utf-8')
    content = " ".join(f.readlines())
    contract = ContractParser(content).parse()
    f.close()
    global counter
    counter.value += 1
    print("done.." + str(counter.value))
    return contract


def export_contract_page(pair):
    page_file = pair[0]
    output_file = pair[1]
    contract = parse_contract_page(page_file)

    output = codecs.open(output_file, 'w', 'utf-8')
    output.write(json.dumps(contract) + "\n")
    output.close()


def create_data_set_from_files(path_to_folder, output_folder):
    all_files_in_folder = [(path_to_folder + "/" + f, output_folder + "/" + f) for f in listdir(path_to_folder)]
    pool = multiprocessing.Pool(100)
    print("parsing page files....")
    pool.map(export_contract_page, all_files_in_folder)
