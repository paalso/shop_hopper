from shop_hopper.parsers.base_parser import BaseParser


class StariyfantastParser(BaseParser):
    OFFER_SELECTOR = '.productItem'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'STARIYFANTAST',
            'url': 'https://newauction.org/'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.namePI a')

    def _get_image(self, item):
        image_element = item.select_one('.mainImagePI img')
        image_url = image_element.get('src')
        return image_url

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.pricePI')
        price = price_element.getText().split()[1].split('.')[0]
        return price
