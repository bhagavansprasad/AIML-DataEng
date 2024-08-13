import requests
from bs4 import BeautifulSoup
from utils import save_to_file

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_links(self):
        """
        Scrapes the website and returns a list of document links.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Ensure we notice bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all the links to PDFs or documents
            links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.endswith('.pdf') or href.endswith('.docx') or href.endswith('.doc'):
                    links.append(href)
            
            return links

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def save_links_to_file(self, links, filename):
        """
        Saves the list of links to a text file.
        """
        save_to_file(links, filename)
        print(f"Links saved to {filename}.")
