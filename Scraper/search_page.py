# -*- coding: utf-8 -*-
import codecs
import itertools
import multiprocessing
import re
from os import listdir

from Scraper.GeneralMessage import GeneralMessage


def extract_links_from_index_page(content):
    pattern = re.compile(r'/consultas/detalleProceso\.do\?numConstancia=[0-9-]+')
    urls = pattern.findall(content)
    return list(set(urls))


def extract_links_from_file(path_to_file: str):
    print("reading.." + path_to_file)
    try:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            content = f.read()
            f.close()
            return extract_links_from_index_page(content)
    except UnicodeDecodeError:
        GeneralMessage.publishError("Problem of decode with the file: " + path_to_file)



def extract_all_links(path_to_page_folder: str):
    all_files_in_folder = [path_to_page_folder + f for f in listdir(path_to_page_folder)]
    pool = multiprocessing.Pool(50)
    results = pool.map(extract_links_from_file, all_files_in_folder)
    print("concatenating results....")
    results = set(list(itertools.chain(*results)))
    return results


def main(args):
    path_to_folder_with_pages: str = args[0]
    path_to_output_file: str = args[1]
    all_links = extract_all_links(path_to_folder_with_pages)

    output = codecs.open(path_to_output_file, 'w', 'utf-8')
    for link in all_links:
        output.write(link + "\n")
    output.close()

# Extracts all the contract urls from a folder filled with contract pages
# <PathToDownloadedSearchPages> <OutputFile>
# main(["/Users/dav009/source/Scraper/pages/", "/Users/dav009/source/Scraper/all_links"])
