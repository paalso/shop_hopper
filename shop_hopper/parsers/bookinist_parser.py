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
            'name': 'Bukinist',
            'alias': 'bukinist',
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

    def _get_image(self, item):
        image_element = item.select_one('.left-img>.imageOfBook>a>img')
        image_src = image_element.get('src')
        return self._get_full_url(image_src) if image_src else None

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.fleft>.info-sel p:nth-of-type(2)')
        price = (price_element.text.split()[1]).split(',')[0]
        return price
