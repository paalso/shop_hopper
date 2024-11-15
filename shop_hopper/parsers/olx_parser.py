import re
from shop_hopper.parsers.base_parser import BaseParser


class OlxParser(BaseParser):
    NO_OFFERS_MESSAGE = 'Ми знайшли  0 оголошень'
    OFFER_SELECTOR = 'div.css-qfzx1y'
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
        valid_offers = offers[:valid_offers_number]
        return valid_offers

    @staticmethod
    def _get_platform():
        return {
            'name': 'OLX',
            'url': 'https://www.olx.ua'
        }

    def _get_title(self, item):
        title_name = item.select_one('h6').getText()
        title_href = item.find('a').get('href')
        title_url = self._get_full_url(title_href) if title_href else None
        return {
            'name': title_name,
            'url': title_url
        }

    # TODO: Unable to retrieve seller info from the search result page.
    #       We can follow the title_url to get the seller's details.
    def _get_seller(self, item):
        return self.MISSING_ITEM

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
