from bs4 import BeautifulSoup


def _alib_parser(query):
    pass


def _newauction_parser(query):
    "public_offer_snippet_container"


def _olx_parser(query):
    pass


parsers = {
    'alib': _alib_parser,
    'newauction': _newauction_parser,
    'olx': _olx_parser
}
