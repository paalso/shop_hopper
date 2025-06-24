from urllib.parse import quote, quote_plus


def _encode_alib_query(search_query: str) -> str:
    """
    Encodes a search query for the Alib platform using Windows-1251 encoding.

    Args:
        search_query (str): The search query string.

    Returns:
        str: Encoded query URL for Alib.
    """
    encoded_query = search_query.encode('windows-1251')
    url_encoded_query = quote(encoded_query)
    url_encoded_query = url_encoded_query.replace('%20', '+')
    return f'https://alib.top/find3.php?tfind={url_encoded_query}'


QUERY_URL_BUILDERS = {
    'alib': _encode_alib_query,
    'newauction': lambda search_query: (
        f'https://newauction.org/listing/offer/knigi_bukinistika-121818/'
        f'search_{quote_plus(search_query)}'
    ),
    'olx': lambda search_query: (
        f'https://www.olx.ua/uk/hobbi-otdyh-i-sport/knigi-zhurnaly/q-'
        f'{search_query.replace(" ", "-")}/'
    ),
    'unc': lambda search_query: (
        f'https://unc.ua/uk/auction?search={quote_plus(search_query)}'
        f'&andor_type=and&truncation=true&'
        f'search_content[]=name&cat=2024&sort=price'
    ),
    'promua': lambda search_query: (
        f'https://prom.ua/ua/search?search_term={quote_plus(search_query)}'
    ),
    'stariyfantast': lambda search_query: (
        f'https://stariyfantast.ua.market/search?query='
        f'{quote_plus(search_query)}'
    ),
    'skylots': lambda search_query: (
        f'https://skylots.org/search.php?search={quote_plus(search_query)}'
        f'&seller_id=0&desc_check=0&catid=121818'
    ),
    'violity': lambda search_query: (
        f'https://violity.com/ru/search/result?auction_id=497&query='
        f'{search_query}&filter=1&phrase=1&title=on&desc=on'
    ),
}


def build_query_url(platform: str, search_query: str) -> str:
    """
    Builds a query URL for a specified platform.

    Args:
        platform (str): The name of the platform.
        search_query (str): The search query string.

    Returns:
        str: The generated query URL.
    """
    builder = QUERY_URL_BUILDERS.get(
        platform,
        lambda search_query: f'https://default.search.com?q='
                             f'{quote_plus(search_query)}'
    )
    return builder(search_query)
