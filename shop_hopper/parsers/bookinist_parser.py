import re
from shop_hopper.parsers.base_parser import BaseParser


class BookinistParser(BaseParser):
    OFFER_SELECTOR = 'one-book'
    REGEX_TITLE_CLEANER = re.compile(r'\s+')

    def _get_offers(self):
        return self.soup.find_all('div', class_=self.OFFER_SELECTOR)

    @staticmethod
    def _get_platform():
        return {
            'name': 'Bookinist',
            'url': 'https://www.bukinist.in.ua/'
        }

    def _get_title(self, item):
        title_element = item.find('div', class_='right-descr').find('p')
        title_name = self.REGEX_TITLE_CLEANER.sub(
            ' ', title_element.text.strip())
        title_url = item.find('a', class_='button').get('href')
        return {
            'name': title_name,
            'url': title_url
        }

    def _get_seller(self, item):
        return self._get_name_and_url(item, '.fleft>.info-sel a')

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.popupInfo.info-sel.a-center p')
        price = (price_element.getText().split()[1]).split(',')[0]
        return price
