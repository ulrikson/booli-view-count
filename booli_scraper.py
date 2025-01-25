import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional


class BooliScraper:
    """A scraper for Booli property listings."""

    BASE_URL = "https://www.booli.se/bostad/{}"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        )

    def get_property_details(self, property_id: str) -> Optional[Dict]:
        """
        Fetch and parse property details from Booli.

        Args:
            property_id: The Booli property ID

        Returns:
            Dictionary containing property details or None if failed
        """
        try:
            url = self.BASE_URL.format(property_id)
            response = self.session.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            view_count = self._extract_view_count(soup)

            return {
                "url": url,
                "title": self._safe_extract(soup, "h1"),
                "view_count": view_count,
            }

        except requests.RequestException:
            return None
        except Exception:
            return None

    def _safe_extract(self, soup: BeautifulSoup, selector: str) -> str:
        """Safely extract text from a BeautifulSoup element."""
        element = soup.find(selector)
        return element.text.strip() if element else ""

    def _extract_view_count(self, soup: BeautifulSoup) -> Optional[int]:
        """Extract the view count from the page."""
        try:
            # Find all div elements with class info-point
            info_points = soup.find_all("div", class_="info-point")

            # Look through each info-point div for the one containing sidvisningar
            for info_point in info_points:
                # Look for the text within article-typography div
                typography_div = info_point.find("div", class_="article-typography")
                if typography_div and "sidvisningar" in typography_div.text.lower():
                    # Extract the number from the strong tag
                    strong_tag = typography_div.find("strong")
                    if strong_tag:
                        return int(strong_tag.text.strip())

            return None
        except Exception:
            return None
