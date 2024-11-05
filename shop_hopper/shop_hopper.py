import requests
from shop_hopper.query_generators import query_generators
from shop_hopper.parsers import parsers

DEFAULT_PLATFORMS = 'alib', 'newauction', 'olx'
DEFAULT_PLATFORMS = 'newauction',
DEFAULT_PLATFORMS = ('alib',)


class ShopHopper:
    def __init__(self, platforms=DEFAULT_PLATFORMS):
        self.platforms = platforms

    def search(self, request):
        for platform in self.platforms:
            query_generator = query_generators.get(platform)
            if not query_generator:
                print(f"Warning: No query generator found for {platform}.")
                continue

            query_url = query_generator(request)
            print(f"Searching in {platform}: {query_url}")

            parser = parsers.get(platform)
            if not parser:
                print(f"Warning: No parser found for {platform}.")
                continue

            response = requests.get(query_url)
            print(response.text)
            print(f'response: {response}')
            print(f'response.text: {response.text}')
            # print(f'response: {response}')
            if response.ok:
                response_content = response.text
                parse_result = parser(response_content)

        return 'Oops!'
