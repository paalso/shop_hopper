from shop_hopper.config.platforms import (
    VIA_SELENIUM_FETCH_CONTENT_PLATFORMS,
    resolve_platform_alias
)
from shop_hopper.via_selenium_fetch_content import \
    ContentFetcher as SeleniumContentFetcher
from shop_hopper.response_fetcher import ResponseFetcher
from shop_hopper.query_url_biulders import build_query_url


class ContentFetcher:
    def __init__(self, logger):
        self.logger = logger

    def fetch_content(self, platform, search_query):
        base_platform = resolve_platform_alias(platform)

        if base_platform in VIA_SELENIUM_FETCH_CONTENT_PLATFORMS:
            content_fetcher = SeleniumContentFetcher(self.logger)
            content = content_fetcher.fetch_content(search_query)
            query_url = build_query_url(base_platform, search_query)
        else:
            response_fetcher = ResponseFetcher(self.logger).get_response
            response = response_fetcher(platform, search_query)
            query_url = response.url
            content = response.text if response else None

        return content, query_url
