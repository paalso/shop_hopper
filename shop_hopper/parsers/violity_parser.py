from shop_hopper.parsers.base_parser import BaseParser


class ViolityParser(BaseParser):
    OFFER_SELECTOR = '.tr'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'Violity',
            'url': 'https://violity.com/ua'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.title a')

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.current p')
        price = price_element.getText()
        return price

    def _get_image(self, item):
        img_element = item.select_one('img')

        img_url = img_element.get('src')
        return img_url
