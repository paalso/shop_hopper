import re
from shop_hopper.parsers.base_parser import BaseParser


class OlxParser(BaseParser):
    NO_OFFERS_MESSAGE = 'Ми знайшли  0 оголошень'
    OFFER_SELECTOR = '.css-j0t2x2'
    INT_NUMBER_REGEX = re.compile(r'\d+')

    def parse(self):
        if self.NO_OFFERS_MESSAGE in self.soup.text:
            return []

        return super().parse()

    def _get_offers(self):
        offers = self.soup.select(self.OFFER_SELECTOR)
        valid_offers_count_element = (
            self.soup.select_one('[data-testid="total-count"]'))
        valid_offers_number = int(self.INT_NUMBER_REGEX.search(
            valid_offers_count_element.getText()).group(0))
        if valid_offers_number == 0:
            return []

        valid_offers = [
            item for item in offers[0]
            if item.get('data-cy') == 'l-card'
        ]

        return valid_offers

    @staticmethod
    def _get_platform():
        return {
            'name': 'OLX',
            'alias': 'olx',
            'url': 'https://www.olx.ua'
        }

    def _get_title(self, item):
        title_name = item.select_one('h4').getText()
        title_href = item.find('a').get('href')
        title_url = self._get_full_url(title_href) if title_href else None
        return {
            'name': title_name,
            'url': title_url
        }

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('p', attrs={'data-testid': 'ad-price'})
        price = ''.join(price_element.getText().split()[:-1])
        return price

    def _get_image(self, offer):
        img_element = offer.select_one('img')

        img_url = img_element.get('src')

        # if "no_thumbnail" in img_url:
        #     srcset = img_element.get('srcset')
        #     if srcset:
        #         img_url = srcset.split(",")[0].split()[0]
        #
        # print(f"Получен URL изображения: {img_url}")
        return img_url
