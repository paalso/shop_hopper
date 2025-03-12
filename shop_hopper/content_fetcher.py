from shop_hopper.config.platforms import (
    VIA_SELENIUM_FETCH_CONTENT_PLATFORMS,
    resolve_platform_alias
)
from shop_hopper.via_selenium_content_fetcher import \
    ContentFetcher as SeleniumContentFetcher
from shop_hopper.response_fetcher import ResponseFetcher


class ContentFetcher:
    def __init__(self, logger):
        self.logger = logger

    def fetch_content(self, platform, search_query):
        base_platform = resolve_platform_alias(platform)

        if base_platform in VIA_SELENIUM_FETCH_CONTENT_PLATFORMS:
            content_fetcher = SeleniumContentFetcher(self.logger)
            content, query_url = content_fetcher.fetch_content(search_query)
            return content, query_url

        response_fetcher = ResponseFetcher(self.logger).get_response
        response = response_fetcher(platform, search_query)

        if response:
            query_url = response.url
            content = response.text if response else None
        else:
            self.logger.warning(f'{platform}: No content fetched')
            query_url = None
            content = None

        return content, query_url
