PLATFORM_ALIASES = {
    'alib': 'alib',
    'newauction': 'newauction',
    'olx': 'olx',
    'bukinist': 'bukinist',
    'bookinist': 'bukinist',
    'unc': 'unc',
    'prom': 'promua',
    'promua': 'promua',
    'stariyfantast': 'stariyfantast',
    'staryfantast': 'stariyfantast',
    'skylots': 'skylots',
    'violity': 'violity',
}

VIA_SELENIUM_FETCH_CONTENT_PLATFORMS = 'violity',
POST_REQUEST_PLATFORMS = 'bukinist',
GET_REQUEST_PLATFORMS = tuple(
    set(PLATFORM_ALIASES.values()) -
    set(POST_REQUEST_PLATFORMS + POST_REQUEST_PLATFORMS)
)

ALL_SUPPORTED_PLATFORMS = (
    GET_REQUEST_PLATFORMS +
    POST_REQUEST_PLATFORMS +
    VIA_SELENIUM_FETCH_CONTENT_PLATFORMS
)


def resolve_platform_alias(platform_alias):
    return PLATFORM_ALIASES[platform_alias]
