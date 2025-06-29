from shop_hopper.parsers.base_parser import BaseParser


class UncParser(BaseParser):
    OFFER_SELECTOR = '.catalog_card'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'UNC',
            'alias': 'unc',
            'url': 'https://unc.ua/'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.catalog_card__title')

    def _get_image(self, item):
        image_element = item.select_one('.catalog_card__image_cnt img')
        image_url = image_element.get('data-original')
        return image_url

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.catalog_card__price span')
        price = price_element.getText().split()[0]
        return price
