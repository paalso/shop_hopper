import json

from shop_hopper.parsers.base_parser import BaseParser


class NewauctionParser(BaseParser):
    OFFER_SELECTOR = '.public_offer_snippet_wrapper'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'NewAuction',
            'alias': 'newauction',
            'url': 'https://newauction.org/'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.offer_snippet_body_top--title')

    def _get_seller(self, item):
        return self._get_name_and_url(item, '.about_user a')

    def _get_image(self, item):
        image_element = item.select_one('.snippet_photo')
        data_img = image_element.get('data-img')
        urls = json.loads(data_img)
        if urls:
            first_url = urls[0]
            return first_url

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.offer_snippet_body_price--value val')
        price = price_element.getText()
        return price
