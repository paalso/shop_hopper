import shop_hopper.response_fetchers.get_fetchers as get_fetchers
import shop_hopper.response_fetchers.post_fetchers as post_fetchers
from shop_hopper.config.constants import VALID_PLATFORMS

post_request_platforms = 'bookinist',
get_request_platforms = 'alib', 'newauction', 'olx', 'unc', 'prom', 'promua'


def _get_base_platform(platform_alias):
    return VALID_PLATFORMS[platform_alias]


def get_response_fetcher(platform: str):
    platform = _get_base_platform(platform)
    if platform in post_request_platforms:
        return post_fetchers.fetch_response(platform)
    elif platform in get_request_platforms:
        return get_fetchers.fetch_response(platform)
