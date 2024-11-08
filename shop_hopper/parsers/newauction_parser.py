from shop_hopper.parsers.base_parser import BaseParser


class NewauctionParser(BaseParser):
    def parse(self):
        offers = self.soup.find_all('div', class_='offer_snippet--body')

        results = []

        for offer in offers:
            platform = self.__class__._get_platform()
            title = self._get_title(offer)
            price = self.__class__._get_price(offer)
            seller = self._get_seller(offer)

            results.append({
                'platform': platform,
                'title': title,
                'price': price,
                'seller': seller,
            })

        return results

    @staticmethod
    def _get_platform():
        return {
            'name': 'NewAuction',
            'url': 'https://newauction.org/'
        }

    def _get_title(self, item):
        return self._get_name_and_url(item, '.offer_snippet_body_top--title')

    def _get_seller(self, item):
        return self._get_name_and_url(item, '.about_user a')

    def _get_name_and_url(self, item, selector):
        element = item.select_one(selector)
        if not element:
            return {'name': None, 'url': None}

        name = element.getText().strip()
        href = element.get('href')

        url = f'{self.base_url}{href}' if href else None

        return {
            'name': name,
            'url': url
        }

    @staticmethod
    def _get_price(item):
        price_element = item.select_one('.offer_snippet_body_price--value val')
        price = price_element.getText()
        return price
