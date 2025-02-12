from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

class BilalScraped:
    def __init__(self):
        self.base_url = "https://www.tempusopen.se/swimmers/313706/swimming"
        self.driver_path = "path/to/chromedriver"  # Update this with the path to your chromedriver
        self.driver = webdriver.Chrome(service=Service(self.driver_path))

    def fetch_main_page(self):
        """Fetches and parses the main page using Selenium."""
        self.driver.get(self.base_url)
        time.sleep(3)  # Wait for the JavaScript content to load
        self.soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def outer_scraper(self):
        """Scrapes strokes and times."""
        self.fetch_main_page()
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
                print(f"{stroke}: {stroke_time}")

        self.driver.quit()  # Close the browser
        return strokes, times


if __name__ == '__main__':
    scraper = BilalScraped()
    scraper.outer_scraper()
