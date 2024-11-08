from shop_hopper.parsers.base_parser import BaseParser


class OlxParser(BaseParser):
    def parse(self):
        offers = self.soup.find_all(
            "div", attrs={"data-cy": "l-card", "data-testid": "l-card"})

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
            'name': 'OLX',
            'url': 'https://www.olx.ua'
        }

    def _get_title(self, item):
        title_name = item.select_one('h6').getText()
        title_href = item.find('a').get('href')
        title_url = f'{self.base_url}{title_href}' if title_href else None
        return {
            'name': title_name,
            'url': title_url
        }

    # TODO: Unable to retrieve seller info from the search result page.
    #       We can follow the title_url to get the seller's details.
    def _get_seller(self, item):
        return {
            'name': None,
            'url': None
        }

    @staticmethod
    def _get_price(item):
        price_element = item.select_one("p", attrs={"data-testid": "ad-price"})
        price = price_element.getText().split()[0]
        return price
