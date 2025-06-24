from shop_hopper.parsers.base_parser import BaseParser


class PromUaParser(BaseParser):
    OFFER_SELECTOR = '[data-qaid="product_block"]'

    def _get_offers(self):
        return self.soup.select(self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'Prom.ua',
            'alias': 'promua',
            'url': 'https://prom.ua/'
        }

    def _get_title(self, item):
        title_element = item.select_one('[data-qaid="product_link"]')
        title_name = title_element.get('title')
        title_href = title_element.get('href')
        title_url = self._get_full_url(title_href)
        return {
            'name': title_name,
            'url': title_url
        }

    def _get_seller(self, item):
        seller_element = item.select_one('[data-qaid="company_link"]>a')
        if not seller_element:
            return self.MISSING_ITEM

        seller_name = seller_element.get('title')
        seller_href = seller_element.get('href')
        seller_url = self._get_full_url(seller_href)
        return {
            'name': seller_name,
            'url': seller_url
        }

    def _get_image(self, item):
        image_element = item.select_one('[data-qaid="product_link"] img')
        image_url = image_element.get('src')
        return image_url

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('[data-qaid="product_price"]')
        price = price_element.get('data-qaprice')
        return price
