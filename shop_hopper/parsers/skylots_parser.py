from shop_hopper.parsers.base_parser import BaseParser


class SkyLotsParser(BaseParser):
    OFFER_SELECTOR = '.search_lot'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'SkyLots',
            'url': 'https://skylots.org/'
        }

    def _get_title(self, item):
        title_element = item.select_one('a.search_lot_link')
        title_name = title_element.get('title')
        title_href = title_element.get('href')
        title_url = self._get_full_url(title_href)
        return {
            'name': title_name,
            'url': title_url
        }

    def _get_seller(self, item):
        return self._get_name_and_url(
            item, '.seller')

    def _get_image(self, item):
        image_element = item.select_one('img.searchimg')
        image_url = image_element.get('src')
        if image_url:
            return image_url
        image_url = image_element.get('data-src')
        return image_url

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.search_lot_price')
        price = price_element.getText().split('.')[0]
        return price
