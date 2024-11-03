import urllib.parse


query_generators = {
    'alib': lambda request:
        f'https://alib.top/find3.php?tfind={encode_alib_request(request)}',
    'newauction': lambda request:
        f'https://newauction.org/listing/offer/search_'
        f'{urllib.parse.quote_plus(request)}',
    'olx': lambda request:
        f'https://www.olx.ua/uk/list/q-{urllib.parse.quote_plus(request)}/'
}


def encode_alib_request(request):
    byte_string = request.encode('windows-1251')
    return urllib.parse.quote(byte_string)
