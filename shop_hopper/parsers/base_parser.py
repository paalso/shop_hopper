from abc import abstractmethod
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class BaseParser:
    """
    A base parser for extracting product information from various platforms.

    Child classes must implement methods to extract the title, price, seller,
    and list of offers according to the specific structure of each platform.
    """
    def __init__(self, html, query):
        # Extracts the base URL from the query URL
        self.base_url = self.__class__._get_base_url(query)
        # Initializes BeautifulSoup for parsing HTML content
        self.soup = BeautifulSoup(html, 'html.parser')

    def parse(self):
        """
        Extracts a list of product offers with details on platform, title,
        price, and seller.

        Returns:
            list[dict]: A list of dictionaries containing offer data.
        """
        offers = self._get_offers()

        return [
            {
                'platform': self._get_platform(),
                'title': self._get_title(offer),
                'price': self._get_price(offer),
                'seller': self._get_seller(offer),
            }
            for offer in offers
        ]

    @abstractmethod
    def _get_offers(self):
        """
        Should be implemented in the subclass.
        Returns a list of offer elements from the HTML content.
        """
        pass

    @staticmethod
    @abstractmethod
    def _get_platform():
        """
        Should be implemented in the subclass.
        Returns the platform name and base url
        """
        pass

    @abstractmethod
    def _get_title(self, offer):
        """
        Should be implemented in the subclass.
        Extracts the title of the offer.
        """
        pass

    @abstractmethod
    def _get_price(self, offer):
        """
        Should be implemented in the subclass.
        Extracts the price of the offer.
        """
        pass

    @abstractmethod
    def _get_seller(self, offer):
        """
        Should be implemented in the subclass.
        Extracts the seller information from the offer.
        """
        pass

    @staticmethod
    def _get_base_url(query):
        """
        Extracts the base URL (scheme + domain) from a full query URL.
        For example:
        'https://example.com/search?q=item' -> 'https://example.com'.
        """
        parsed_url = urlparse(query)
        return f'{parsed_url.scheme}://{parsed_url.netloc}'
