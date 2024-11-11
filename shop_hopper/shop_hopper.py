import requests
from shop_hopper.query_generators import query_generators
from shop_hopper.parsers.parsers import parsers

# Default list of platforms to search on if none are specified.
DEFAULT_PLATFORMS = 'newauction', 'olx'
DEFAULT_TIMEOUT = 10


class ShopHopper:
    """
    Main class for searching products across multiple e-commerce platforms.
    Uses query generators to build search URLs and parsers
    to extract product data.
    """

    def __init__(self, logger, platforms=DEFAULT_PLATFORMS):
        """
        Initializes the ShopHopper instance.

        Args:
            logger (Logger): A logging instance for handling logs.
            platforms (tuple): A tuple of platform names to search on.
        """
        self.platforms = platforms
        self.logger = logger

    def search(self, request):
        """
        Searches for products based on the given request across
        the specified platforms.

        Args:
            request (str): The search query string (e.g., product name).

        Returns:
            list[dict]: A list of dictionaries containing parsed product
            offers from all platforms.
        """
        result = []

        for platform in self.platforms:
            query_generator, parser_class = (
                self._get_query_and_parser(platform))
            if not query_generator or not parser_class:
                continue

            query_url = query_generator(request)
            self.logger.info(f'Searching in {platform}: {query_url}')

            try:
                response = requests.get(query_url, timeout=DEFAULT_TIMEOUT)

                if not response.ok:
                    self.logger.error(
                        f'Error occurred while fetching {query_url}: '
                        f'{response.status_code} - {response.text}')
                    continue

                parse_result = parser_class(response.text, query_url).parse()
                result.extend(parse_result)
                self.logger.info(
                    f'Parsed {len(parse_result)} offers from {platform}')

            except requests.exceptions.RequestException as e:
                self.logger.error(
                    f'Request failed for {platform} ({query_url}): {e}')
                continue
        return result

    def _get_query_and_parser(self, platform):
        """
        Retrieves the query generator and parser class for a given platform.

        Args:
            platform (str): The platform name.

        Returns:
            tuple: A tuple containing the query generator and parser.
                   Returns (None, None) if either is missing.
        """
        query_generator = query_generators.get(platform)
        if not query_generator:
            self.logger.warning(f'No query generator found for {platform}')
            return None, None

        parser_class = parsers.get(platform)
        if not parser_class:
            self.logger.warning(f'No parser found for {platform}')
            return None, None

        return query_generator, parser_class
