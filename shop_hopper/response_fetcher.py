import requests
from shop_hopper.query_url_biulders import build_query_url
from shop_hopper.config.platforms import (
    GET_REQUEST_PLATFORMS,
    POST_REQUEST_PLATFORMS,
    resolve_platform_alias
)

TIMEOUT = 10


class ResponseFetcher:
    ALIB_REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    PLATFORM_ENCODINGS = {
        'alib': 'windows-1251',
        'olx': 'utf-8'
    }

    def __init__(self, logger, timeout=TIMEOUT):
        self.logger = logger
        self.timeout = timeout

    def get_response(self, platform, search_query):
        base_platform = resolve_platform_alias(platform)
        if base_platform in POST_REQUEST_PLATFORMS:
            return self._fetch_from_bookinist(search_query)
        elif base_platform in GET_REQUEST_PLATFORMS:
            return self._fetch_get_response(base_platform, search_query)

    def _fetch_from_bookinist(self, search_query):
        url = 'https://www.bukinist.in.ua/books/find'
        payload = {'data[Find][username]': search_query, '_method': 'POST'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        try:
            response = requests.post(
                url, data=payload, headers=headers, timeout=self.timeout)
            return response
        except requests.RequestException:
            raise

    def _fetch_get_response(self, platform: str, search_query: str):
        query_url = build_query_url(platform, search_query)
        self.logger.debug(f'Query :{query_url}')
        headers = self.ALIB_REQUEST_HEADERS if platform == 'alib' else {}

        try:
            response = requests.get(
                query_url, headers=headers, timeout=self.timeout)

            if not response.ok:
                self.logger.error(
                    f'Error occurred while fetching from {platform}: '
                    f'{response.status_code} - {response.text}'
                )

            response.encoding = self.PLATFORM_ENCODINGS.get(platform)

        except requests.exceptions.RequestException as e:
            self.logger.error(f'Request failed for {platform}: {e}')
            response = None

        return response
