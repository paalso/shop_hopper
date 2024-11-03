import yaml
from  shop_hopper.query_generators import query_generators


class ShopHopper:
    def __init__(self, settings_path='shop_hopper/config/platforms.yaml'):
        self.settings = self.__class__._load_settings(settings_path)

    def search(self, request):
        for setting in self.settings:
            platform = setting['platform']
            parser = setting['parser']
            print(platform, parser)
            http_request = self.__class__._generate_query(platform, request)
            print(http_request)
            print()
        return 'Oops!'

    @staticmethod
    def _load_settings(filepath):
        with open(filepath, 'r') as f:
            settings = yaml.safe_load(f)
        return settings

    @staticmethod
    def _generate_query(platform, request):
        return query_generators[platform](request)
