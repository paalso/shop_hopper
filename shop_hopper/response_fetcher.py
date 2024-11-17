import requests
import urllib.parse
from shop_hopper.config.constants import VALID_PLATFORMS
from urllib.parse import quote, quote_plus


class ResponseFetcher:
    POST_REQUEST_FETCHERS = 'bookinist',
    GET_REQUEST_PLATFORMS = (set(VALID_PLATFORMS.values()) -
                             set(POST_REQUEST_FETCHERS))

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

    QUERY_URL_BUILDERS = {
        'alib': lambda request: ResponseFetcher._encode_alib_query(request),
        'newauction': lambda request: (
            f'https://newauction.org/listing/offer/knigi_bukinistika-121818/'
            f'search_{urllib.parse.quote_plus(request)}'
        ),
        'olx': lambda request: (
            f'https://www.olx.ua/uk/hobbi-otdyh-i-sport/knigi-zhurnaly/q-'
            f'{request.replace(" ", "-")}/'
        ),
        'unc': lambda request: (
            f'https://unc.ua/uk/auction?search={quote_plus(request)}'
            f'&andor_type=and&truncation=true&'
            f'search_content[]=name&cat=2024&sort=price'
        ),
        'promua': lambda request: (
            f'https://prom.ua/ua/search?search_term={quote_plus(request)}'
        ),

        'stariyfantast': lambda request: (
            f'https://stariyfantast.ua.market/search?query='
            f'{quote_plus(request)}')
    }

    PLATFORM_ENCODINGS = {
        'alib': 'windows-1251',
        'olx': 'utf-8'
    }

    def __init__(self, logger, timeout):
        self.logger = logger
        self.timeout = timeout

    def get_response(self, platform, request):
        base_platform = self._get_base_platform(platform)

        if base_platform in self.POST_REQUEST_FETCHERS:
            return self._fetch_from_bookinist(request)
        elif base_platform in self.GET_REQUEST_PLATFORMS:
            return self._fetch_get_response(base_platform, request)

    @staticmethod
    def _get_base_platform(platform_alias):
        return VALID_PLATFORMS[platform_alias]

    def _fetch_from_bookinist(self, request):
        url = 'https://www.bukinist.in.ua/books/find'
        payload = {'data[Find][username]': request, '_method': 'POST'}
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

    @staticmethod
    def _encode_alib_query(request: str) -> str:
        encoded_query = request.encode('windows-1251')
        url_encoded_query = quote(encoded_query)
        url_encoded_query = url_encoded_query.replace('%20', '+')
        return f'https://alib.top/find3.php?tfind={url_encoded_query}'

    def _fetch_get_response(self, platform: str, query: str):
        query_url_builder = self.QUERY_URL_BUILDERS.get(platform)

        if not query_url_builder:
            raise ValueError(f'Unsupported platform: {platform}')

        query_url = query_url_builder(query)
        self.logger.debug(f'Query :{query_url}')
        headers = self.ALIB_REQUEST_HEADERS if platform == 'alib' else {}

        try:
            response = requests.get(
                query_url, headers=headers, timeout=self.timeout)
            response.encoding = self.PLATFORM_ENCODINGS.get(platform)
            return response
        except requests.RequestException:
            raise
