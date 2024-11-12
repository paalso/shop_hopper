from shop_hopper.parsers.newauction_parser import NewauctionParser
from shop_hopper.parsers.olx_parser import OlxParser
from shop_hopper.parsers.alib_parser import AlibParser

parsers = {
    'newauction': NewauctionParser,
    'olx': OlxParser,
    'alib': AlibParser
}
