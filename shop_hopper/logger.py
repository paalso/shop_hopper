import os
import logging
from dotenv import load_dotenv


class Logger:
    def __init__(self):
        load_dotenv()
        self.logger = self._setup_logger()

    def get_logger(self):
        return self.logger

    @staticmethod
    def _setup_logger():
        debug_mode = os.getenv("ENV") == "development"
        logging.basicConfig(
            level=logging.DEBUG if debug_mode else logging.INFO)
        return logging.getLogger(__name__)
