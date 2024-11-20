from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from shop_hopper.query_url_biulders import build_query_url

TIMEOUT = 3  # Default timeout in seconds


class ContentFetcher:
    """
    A class to fetch HTML content from e-commerce platforms using Selenium.

    Attributes:
        logger: Logger instance for logging messages.
        timeout: Time to wait for page loading or element appearance.
        driver: Selenium WebDriver instance.
    """

    def __init__(self, logger, timeout=TIMEOUT):
        """
        Initializes the ContentFetcher with a logger and timeout.

        Args:
            logger: Logger instance for logging messages.
            timeout (int): Timeout in seconds for page loading.
        """
        self.logger = logger
        self.timeout = timeout
        self.driver = self._initialize_driver()

    @staticmethod
    def _initialize_driver():
        """Initialize the Chrome WebDriver with options."""
        options = Options()
        options.headless = True  # Run browser in headless mode (no UI)
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def fetch_content(self, platform, request):
        """
        Fetch the HTML content of the page for a specific platform and request.

        Args:
            platform (str): The platform to search.
            request (str): The search query string.

        Returns:
            str: The page source HTML, or None if fetching failed.
        """
        query_url = build_query_url(platform, request)
        self.logger.debug(f'Query URL: {query_url}')

        try:
            self.driver.get(query_url)
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            content = self.driver.page_source
            self.logger.info(f"Successfully fetched content from {platform}")

        except Exception as e:
            self.logger.error(f"Failed to fetch content from {platform}: {e}")
            content = None

        return content, query_url

    def close(self):
        """Terminate the WebDriver session."""
        if self.driver:
            self.driver.quit()
