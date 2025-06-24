from shop_hopper.parsers.parsers import parsers
from shop_hopper.content_fetcher import ContentFetcher
from shop_hopper.config.platforms import ALL_SUPPORTED_PLATFORMS


class ShopHopper:
    """
    Main class for searching products across multiple e-commerce platforms.
    Uses query generators to build search URLs and parsers
    to extract product data.
    """

    def __init__(self, logger, platforms=ALL_SUPPORTED_PLATFORMS):
        """
        Initializes the ShopHopper instance.

        Args:
            logger (Logger): A logging instance for handling logs.
            platforms (tuple): A tuple of platform names to search on.
        """
        self.platforms = platforms
        self.logger = logger
        self.content_fetcher = ContentFetcher(self.logger)

    def \
            search(self, request):
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

            content, url = self.content_fetcher.fetch_content(
                platform, request)

            if not content:
                self.logger.warning('No content found')
                continue

            self.logger.debug(f'Successfully fetched content from {platform}')
            parse_result = parser_class(content, url).parse()
            result.extend(parse_result)
            self.logger.debug(
                f'Parsed {len(parse_result)} offers from {platform}')

        return result
