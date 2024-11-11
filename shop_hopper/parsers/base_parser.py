from abc import abstractmethod
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class BaseParser:
    """
    A base parser for extracting product information from various platforms.

    Child classes must implement methods to extract the title, price, seller,
    and list of offers according to the specific structure of each platform.
    """
    def __init__(self, html, query):
        """
        Initializes the parser with HTML content and the search query URL.

        Args:
            html (str): HTML content of the page.
            query (str): Search query URL used to determine the base URL.
        """
        self.base_url = self.__class__._get_base_url(query)
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
        Extracts offer elements from the HTML content.

        Should be implemented in the subclass.

        Returns:
            list: A list of HTML elements representing product offers.
        """
        pass

    @staticmethod
    @abstractmethod
    def _get_platform():
        """
        Returns the platform name.

        Should be implemented in the subclass.

        Returns:
            str: The name of the platform.
        """
        pass

    @abstractmethod
    def _get_title(self, offer):
        """
        Extracts the title of the offer.

        Should be implemented in the subclass.

        Returns:
            str: The product title.
        """
        pass

    @abstractmethod
    def _get_price(self, offer):
        """
        Extracts the price of the offer.

        Should be implemented in the subclass.

        Returns:
            str: The product price.
        """
        pass

    @abstractmethod
    def _get_seller(self, offer):
        """
        Extracts the seller information from the offer.

        Should be implemented in the subclass.

        Returns:
            str: The seller name.
        """
        pass

    def _get_picture(self, offer):
        """
        Extracts the picture information from the offer.

        Might be implemented in the subclass.

        Returns:
            str: The seller name.
        """
        return {

        }

    @staticmethod
    def _get_base_url(query):
        """
        Extracts the base URL (scheme + domain) from a full query URL.

        For example:
        'https://example.com/search?q=item' -> 'https://example.com'.

        Args:
            query (str): The full query URL.

        Returns:
            str: The base URL of the platform.
        """
        parsed_url = urlparse(query)
        return f'{parsed_url.scheme}://{parsed_url.netloc}'

    def _get_full_url(self, partial_url):
        """
        Constructs a full URL from a partial URL using the base URL.

        Args:
            partial_url (str): The relative or partial URL.

        Returns:
            str: The complete URL.
        """
        return urljoin(self.base_url, partial_url)

    def _get_name_and_url(self, item, selector):
        """
        Extracts the name and URL of an element based on a CSS selector.

        Args:
            item (element.Tag): The HTML element to search within.
            selector (str): The CSS selector for extracting the element.

        Returns:
            dict: A dictionary containing 'name' and 'url' keys.
        """
        element = item.select_one(selector)
        if not element:
            return {'name': None, 'url': None}

        name = element.getText().strip()
        href = element.get('href')
        url = self._get_full_url(href) if href else None

        return {
            'name': name,
            'url': url
        }
