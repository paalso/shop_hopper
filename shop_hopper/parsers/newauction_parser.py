from shop_hopper.parsers.base_parser import BaseParser


class NewauctionParser(BaseParser):
    OFFER_SELECTOR = 'offer_snippet--body'

    def _get_offers(self):
        return self.soup.find_all('div', class_=self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'NewAuction',
            'url': 'https://newauction.org/'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.offer_snippet_body_top--title')

    def _get_seller(self, item):
        return self._get_name_and_url(item, '.about_user a')

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.offer_snippet_body_price--value val')
        price = price_element.getText()
        return price
