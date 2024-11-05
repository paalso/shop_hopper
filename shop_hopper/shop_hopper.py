import logging
import requests
from shop_hopper.logger import Logger
from shop_hopper.query_generators import query_generators
from shop_hopper.parsers import parsers

DEFAULT_PLATFORMS = 'newauction',
DEFAULT_PLATFORMS = ('alib',)
DEFAULT_PLATFORMS = 'alib', 'newauction', 'olx'


class ShopHopper:
    def __init__(self, platforms=DEFAULT_PLATFORMS):
        self.platforms = platforms
        self.logger = Logger().get_logger()

    def search(self, request):
        for platform in self.platforms:
            query_generator = query_generators.get(platform)
            if not query_generator:
                self.logger.warning(f"No query generator found for {platform}")
                continue

            query_url = query_generator(request)
            self.logger.info(f"\n\nSearching in {platform}: {query_url}")

            parser = parsers.get(platform)
            if not parser:
                self.logger.warning(f"No parser found for {platform}")
                continue

            response = requests.get(query_url)
            if response.ok:
                response_content = response.text
                parse_result = parser(response_content)
            else:
                self.logger.debug(f"response: {response}")
                self.logger.debug(f"response.headers: {response.headers}")

        return 'Oops!'
