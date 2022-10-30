import argparse

from Scraper import contract_spider, search_page, search_page_spider


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="scrape_searchpages | extract_contracts | scrape_contracts | create-dataset")
    parser.add_argument("--input")
    parser.add_argument("--output")
    args = parser.parse_args()

    action = args.action
    input_arg = args.input
    output_arg = args.output

    if action == "scrape_searchpages":
        print("downloading search pages to: %s" % (output_arg))
        search_page_spider.main([output_arg])

    elif action == "extract_contracts":
        print("Reading pages from: %s" % (input_arg))
        print("Saving extracted urls to: %s" % (output_arg))
        search_page.main([input_arg, output_arg])

    elif action == "scrape_contracts":
        print("Reading link list from: %s" % (input_arg))
        print("Download contract html-content: %s" % (output_arg))
        contract_spider.main([input_arg, output_arg])


# Scraper  scrape_searchpages --output folder
# Scraper  extract_contracts --input scrapedSearchPages --output fileWithLinks
# Scraper  scrape_contracts --input fileWithContractLinks --output folderWithContractPages
#
if __name__ == "__main__":
    main()
