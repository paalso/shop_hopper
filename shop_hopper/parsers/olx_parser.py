from shop_hopper.parsers.base_parser import BaseParser


class OlxParser(BaseParser):
    NO_OFFERS_MESSAGE = 'Ми знайшли  0 оголошень'
    OFFER_SELECTOR = {'data-cy': 'l-card', 'data-testid': 'l-card'}

    def parse(self):
        if self.NO_OFFERS_MESSAGE in self.soup.text:
            return []

        return super().parse()

    def _get_offers(self):
        return self.soup.find_all(
            'div', attrs=self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'OLX',
            'url': 'https://www.olx.ua'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, 'h6')

    # TODO: Unable to retrieve seller info from the search result page.
    #       We can follow the title_url to get the seller's details.
    def _get_seller(self, item):
        return {
            'name': None,
            'url': None
        }

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('p', attrs={'data-testid': 'ad-price'})
        price = ''.join(price_element.getText().split()[:-1])
        return price
