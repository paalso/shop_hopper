import requests
from shop_hopper.response_fetchers import fetch_platform_response
from shop_hopper.parsers.parsers import parsers

# Default list of platforms to search on if none are specified.
DEFAULT_PLATFORMS = 'newauction', 'olx', 'alib'
# DEFAULT_PLATFORMS = 'alib',
# DEFAULT_PLATFORMS = 'newauction',
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
            parser_class = parsers.get(platform)
            if not parser_class:
                self.logger.warning(f'No parser found for {platform}')
                continue

            self.logger.info(f'Searching in {platform}')
            try:
                response = fetch_platform_response(platform, request)

                if not response.ok:
                    self.logger.error(
                        f'Error occurred while fetching from {platform}: '
                        f'{response.status_code} - {response.text}'
                    )
                    continue

                parse_result = (
                    parser_class(response.text, response.url).parse())
                result.extend(parse_result)
                self.logger.info(
                    f'Parsed {len(parse_result)} offers from {platform}'
                )

            except requests.exceptions.RequestException as e:
                self.logger.error(
                    f'Request failed for {platform}: {e}'
                )
                continue

        return result
