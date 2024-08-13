from scraper import WebScraper

def main():
    url = "http://example.com"  # Replace with the target URL
    scraper = WebScraper(url)
    links = scraper.scrape_links()

    if links:
        scraper.save_links_to_file(links, "links.txt")
    else:
        print("No links found.")

if __name__ == "__main__":
    main()
