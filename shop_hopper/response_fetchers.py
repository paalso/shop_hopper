from http.client import responses

import requests
import urllib.parse
from urllib.parse import quote

_ALIB_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


def _encode_alib_query(request: str) -> str:
    encoded_query = request.encode('windows-1251')
    url_encoded_query = quote(encoded_query)
    url_encoded_query = url_encoded_query.replace('%20', '+')
    url = f'https://alib.top/find3.php?tfind={url_encoded_query}'
    return url


_query_url_builders = {
    'alib': _encode_alib_query,
    'newauction': lambda request:
        f'https://newauction.org/listing/offer/search_'
        f'{urllib.parse.quote_plus(request)}',
    'olx': lambda request: f'https://www.olx.ua/uk/list/q-'
                           f'{request.replace(" ", "-")}/',
}


def fetch_platform_response(platform: str, query: str):
    query_url_builder = _query_url_builders.get(platform)

    if not query_url_builder:
        raise ValueError(f"Unsupported platform: {platform}")

    query_url = query_url_builder(query)

    headers = _ALIB_REQUEST_HEADERS if platform == 'alib' else {}

    response = requests.get(query_url, headers=headers)
    response.encoding = 'windows-1251' if platform == 'alib' else None

    return response
