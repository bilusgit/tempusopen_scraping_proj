import requests
from bs4 import BeautifulSoup
import time

"""Scrape bilal's times"""


class BilalScraped:
    def __init__(self):
        self.base_url = base_url = "https://www.tempusopen.se/swimmers/313706/swimming"

    def fetch_main_page(self):  # base_url
        # base_url = "https://www.tempusopen.se/swimmers/313706/swimming"
        """Fetches and parses the main page"""
        response = requests.get(self.base_url)  # Skickar en HTTP Get förfrågan
        if response.status_code == 200:
            # BeautifulSoup = parse raw HTML from response,
            # #html.parser = tells BS to use python built in HTML parser to interpret webpage stucture
            self.soup = BeautifulSoup(response.content, "html.parser")
        else:
            raise Exception(f"Failed to fetch {self.base_url}. Status code: {response.status_code}")

    def outer_scraper(self):
        # quotes = self.soup.find_all("span", class_="text")
        rows = self.soup.find_all("tr", class_="even:bg-gray-50")
        times = []
        strokes = []
        for row in rows:
            cells = row.find_all("td", class_="py-2")
            if cells:
                stroke_time = cells[-1].text.strip()
                times.append(stroke_time)
                stroke = cells[0].text.strip()
                strokes.append(stroke)
                print(stroke, f"{stroke_time}")


if __name__ == '__main__':
    scraper = BilalScraped()
    scraper.fetch_main_page()  # Ensure the page is fetched before scraping
    scraper.outer_scraper()
