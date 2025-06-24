from shop_hopper.parsers.base_parser import BaseParser


class ViolityParser(BaseParser):
    OFFER_SELECTOR = 'article.tr'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'Violity',
            'alias': 'violity',
            'url': 'https://violity.com/ua'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.title a')

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.price .current p')
        price = price_element.getText()
        return price

    def _get_seller(self, item):
        seller_element = item.select_one('.seller a')
        if not seller_element:
            return self.MISSING_ITEM

        seller_url = seller_element.get('href')
        seller_name = seller_element.select_one('u').getText()
        return {
            'name': seller_name,
            'url': seller_url
        }

    def _get_image(self, item):
        img_element = item.select_one('img')
        img_url = img_element.get('src')
        return img_url
