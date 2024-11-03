from  shop_hopper.query_generators import query_generators
from  shop_hopper.parsers import parsers
import requests

DEFAULT_PLATFORMS = 'alib', 'newauction', 'olx'


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

            print(query_url)
            print()

        return 'Oops!'


    @staticmethod
    def _generate_query(platform, request):
        return query_generators[platform](request)
