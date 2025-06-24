import re
from shop_hopper.parsers.base_parser import BaseParser


class AlibParser(BaseParser):
    def _get_offers(self):
        paragraphs = self.soup.select('p', recursive=False)
        result = [
            p for p in paragraphs
            if (bold := p.find('b')) and bold == p.contents[0]
            and not self._is_in_excluded_table(p)
        ]

        if result and 'Расширенный поиск' in result[-1].text:
            result.pop()

        return result

    @staticmethod
    def _is_in_excluded_table(element):
        table = element.find_parent('table')
        if table:
            return True
        return False

    @staticmethod
    def _get_platform():
        return {
            'name': 'alib',
            'alias': 'alib',
            'url': 'https://alib.top/'
        }

    def _get_title(self, item):
        item_content = item.text
        title_end_position = item_content.find('г.')
        if title_end_position > 0:
            title_name = item_content[:title_end_position]
        else:
            title_name = item.select_one('b').text
        title_url = self.query
        return {
            'name': title_name,
            'url': title_url
        }

    def _get_seller(self, item):
        seller = self._get_name_and_url(item, 'a')
        if seller.get('name') != 'Купить':
            return seller
        return {
            'name': 'Незарег.',
            'url': None
        }

    @staticmethod
    def _get_price(item):
        regex = re.compile(r'Цена: (\w+) грн')
        return regex.search(item.text).group(1)

    def _get_image(self, item):
        text_tag = item.find(string=re.compile(r'Смотрите:'))
        if not text_tag:
            return None

        image_link = text_tag.find_next('a')
        if image_link and 'href' in image_link.attrs:
            href = image_link['href']
            return href

        return None
