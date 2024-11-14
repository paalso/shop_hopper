from shop_hopper.parsers.alib_parser import AlibParser
from shop_hopper.parsers.bookinist_parser import BookinistParser
from shop_hopper.parsers.newauction_parser import NewauctionParser
from shop_hopper.parsers.olx_parser import OlxParser
from shop_hopper.parsers.unc_parser import UncParser

parsers = {
    'newauction': NewauctionParser,
    'olx': OlxParser,
    'alib': AlibParser,
    'bookinist': BookinistParser,
    'unc': UncParser,
}
