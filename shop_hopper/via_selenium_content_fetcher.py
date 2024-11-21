from shop_hopper.query_url_biulders import build_query_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.options import Options
import time

TIMEOUT = 3
CACHE_VALID_RANGE = 183     # 6 months


class ContentFetcher:
    def __init__(self, logger, timeout=TIMEOUT):
        self.logger = logger
        self.driver = self._initialize_driver()

    def fetch_content(self, search_query):
        return self._get_page_source_from_violity(search_query)

    def _get_page_source_from_violity(self, search_query):
        query_url = build_query_url('violity', search_query)
        self.logger.debug(f'Query :{query_url}')

        try:
            self.driver.get(query_url)
            time.sleep(TIMEOUT)
            content = self.driver.page_source
            self.logger.debug('Successfully fetched content from violity')
            return content, query_url

        except Exception as e:
            self.logger.error(f'Failed to fetch content from Violity: {e}')
            return None, None
        finally:
            self.driver.quit()

    @staticmethod
    def _initialize_driver():  # Configure the browser
        options = Options()
        options.headless = True  # Enable headless mode (no browser window)
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(
                    cache_manager=DriverCacheManager(
                        valid_range=CACHE_VALID_RANGE)
                ).install()
            ),
            options=options,
        )

        driver.execute_cdp_cmd(
            "Network.setBlockedURLs",
            {"urls": ["*.css", "*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg"]},
        )
        driver.execute_cdp_cmd("Network.enable", {})
        return driver
