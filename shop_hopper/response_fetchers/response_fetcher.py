import shop_hopper.response_fetchers.get_fetchers as get_fetchers
import shop_hopper.response_fetchers.post_fetchers as post_fetchers

post_request_platforms = ('bookinist',)
get_request_platforms = ('alib', 'newauction', 'olx')


def get_response_fetcher(platform: str):
    if platform in post_request_platforms:
        return post_fetchers.fetch_response(platform)
    elif platform in get_request_platforms:
        return get_fetchers.fetch_response(platform)
