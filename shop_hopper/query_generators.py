import urllib.parse


query_generators = {
    'alib': lambda request:
        f'https://alib.top/find3.php?tfind={urllib.parse.quote_plus(request)}',
    'newauction': lambda request:
        f'https://newauction.org/listing/offer/search_{urllib.parse.quote_plus(request)}',
    'olx': lambda request:
        f'https://www.olx.ua/uk/list/q-{urllib.parse.quote_plus(request)}/'
}
