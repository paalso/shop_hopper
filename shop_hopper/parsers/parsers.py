from shop_hopper.parsers.alib_parser import AlibParser
from shop_hopper.parsers.bookinist_parser import BookinistParser
from shop_hopper.parsers.newauction_parser import NewauctionParser
from shop_hopper.parsers.olx_parser import OlxParser
from shop_hopper.parsers.promua_parser import PromUaParser
from shop_hopper.parsers.unc_parser import UncParser
from shop_hopper.parsers.stariyfantast_parser import StariyfantastParser
from shop_hopper.parsers.skylots_parser import SkyLotsParser
from shop_hopper.parsers.violity_parser import ViolityParser

parsers = {
    'newauction': NewauctionParser,
    'olx': OlxParser,
    'alib': AlibParser,
    'bookinist': BookinistParser,
    'unc': UncParser,
    'prom': PromUaParser,
    'promua': PromUaParser,
    'stariyfantast': StariyfantastParser,
    'staryfantast': StariyfantastParser,
    'skylots': SkyLotsParser,
    'violity': ViolityParser
}
