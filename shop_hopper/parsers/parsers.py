from shop_hopper.parsers.newauction_parser import NewauctionParser
from shop_hopper.parsers.olx_parser import OlxParser

parsers = {
    'newauction': NewauctionParser,
    'olx': OlxParser,
}
