from bs4 import BeautifulSoup
from urllib.parse import urlparse


class BaseParser:
    def __init__(self, html, query):
        self.base_url = self.__class__._get_base_url(query)
        self.soup = BeautifulSoup(html, 'html.parser')

    @staticmethod
    def _get_base_url(query):
        parsed_url = urlparse(query)
        return f'{parsed_url.scheme}://{parsed_url.netloc}'
