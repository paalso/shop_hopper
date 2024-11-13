import requests


def _fetch_from_bookinist(request):
    url = 'https://www.bukinist.in.ua/books/find'

    payload = {
        'data[Find][username]': request,
        '_method': 'POST'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        return response
    except requests.RequestException:
        raise


_platform_fetchers = {
    'bookinist': _fetch_from_bookinist
}


def fetch_response(platform: str):
    response_fetcher = _platform_fetchers[platform]
    return response_fetcher
