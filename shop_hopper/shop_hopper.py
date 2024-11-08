import requests
from shop_hopper.query_generators import query_generators
from shop_hopper.parsers.parsers import parsers

DEFAULT_PLATFORMS = 'newauction', 'olx'


class ShopHopper:
    def __init__(self, logger, platforms=DEFAULT_PLATFORMS):
        self.platforms = platforms
        self.logger = logger

    def search(self, request):
        result = []

        for platform in self.platforms:
            query_generator = query_generators.get(platform)
            if not query_generator:
                self.logger.warning(f"No query generator found for {platform}")
                continue

            query_url = query_generator(request)
            self.logger.info(f"\n\nSearching in {platform}: {query_url}")

            parser_class = parsers.get(platform)
            if not parser_class:
                self.logger.warning(f"No parser found for {platform}")
                continue

            response = requests.get(query_url)
            if response.ok:
                response_text = response.text
                parse_result = parser_class(response_text, query_url).parse()
                result.extend(parse_result)
            else:
                self.logger.debug(f"response: {response}")
                self.logger.debug(f"response.headers: {response.headers}")

        return result
