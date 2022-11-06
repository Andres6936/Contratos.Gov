import argparse
from enum import Enum, unique

from Scraper import contract_spider, search_page, search_page_spider
from Scraper.GeneralMessage import GeneralMessage
from Server import SimpleServer


# Scraper  scrape_searchpages --output folder
# Scraper  extract_contracts --input scrapedSearchPages --output fileWithLinks
# Scraper  scrape_contracts --input fileWithContractLinks --output folderWithContractPages

@unique
class TypeActions(Enum):
    SCRAPER_SEARCH_PAGE = "scrape_search_pages"
    SCRAPER_CONTRACTS = "scrape_contracts"
    EXTRACT_CONTRACTS = "extract_contracts"
    SERVER_CONTRACTS = "server_contracts"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Transform Load for contracts from government of Colombia")
    parser.add_argument("action", choices=[TypeActions.SCRAPER_SEARCH_PAGE.value, TypeActions.SCRAPER_CONTRACTS.value,
                                           TypeActions.EXTRACT_CONTRACTS.value, TypeActions.SERVER_CONTRACTS.value],
                        help="Generally the order of the arguments should be scrape_searchpages, "
                             "extract_contracts and last scrape_contracts")
    parser.add_argument("-i", "--input", default="Output", type=str)
    parser.add_argument("-o", "--output", default="Output", type=str)
    args = parser.parse_args()

    action: str = args.action
    input_arg: str = args.input
    output_arg: str = args.output

    if action == TypeActions.SCRAPER_SEARCH_PAGE.value:
        GeneralMessage.publish(f"downloading search pages to: {output_arg}")
        search_page_spider.main(output_arg)

    elif action == TypeActions.EXTRACT_CONTRACTS.value:
        GeneralMessage.publish(f"Reading pages from: {input_arg}")
        GeneralMessage.publish(f"Saving extracted urls to: {output_arg}")
        search_page.main(input_arg, output_arg)

    elif action == TypeActions.SCRAPER_CONTRACTS.value:
        GeneralMessage.publish(f"Reading link list from: {input_arg}")
        GeneralMessage.publish(f"Download contract html-content: {output_arg}")
        contract_spider.main(input_arg, output_arg)

    elif action == TypeActions.SERVER_CONTRACTS.value:
        GeneralMessage.publish("Start web server")
        SimpleServer.main()
