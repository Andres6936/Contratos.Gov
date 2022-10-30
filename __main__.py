import argparse

from Scraper import contract_spider, search_page, search_page_spider

# Scraper  scrape_searchpages --output folder
# Scraper  extract_contracts --input scrapedSearchPages --output fileWithLinks
# Scraper  scrape_contracts --input fileWithContractLinks --output folderWithContractPages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Transform Load for contracts from government of Colombia")
    parser.add_argument("action", choices=["scrape_searchpages", "extract_contracts", "scrape_contracts"],
                        help="Generally the order of the arguments should be scrape_searchpages, "
                             "extract_contracts and last scrape_contracts")
    parser.add_argument("-i", "--input", default="Output", type=str)
    parser.add_argument("-o", "--output", default="Output", type=str)
    args = parser.parse_args()

    action: str = args.action
    input_arg: str = args.input
    output_arg: str = args.output

    if action == "scrape_searchpages":
        print(f"downloading search pages to: {output_arg}")
        search_page_spider.main(output_arg)

    elif action == "extract_contracts":
        print(f"Reading pages from: {input_arg}")
        print(f"Saving extracted urls to: {output_arg}")
        search_page.main(input_arg, output_arg)

    elif action == "scrape_contracts":
        print(f"Reading link list from: {input_arg}")
        print(f"Download contract html-content: {output_arg}")
        contract_spider.main(input_arg, output_arg)
