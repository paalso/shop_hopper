from dotenv import load_dotenv
import logging
import os
from rich.logging import RichHandler


DEBUG_ENVS = ('development', 'debug')


class Logger:
    def __init__(self):
        load_dotenv()
        self.logger = self._setup_logger()

    def get_logger(self):
        return self.logger

    @staticmethod
    def _setup_logger():
        current_env = os.getenv('ENV', 'production')
        debug_mode = current_env in DEBUG_ENVS

        if logging.getLogger().hasHandlers():
            return logging.getLogger(__name__)

        logging.basicConfig(
            level=logging.DEBUG if debug_mode else logging.INFO,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True)]
        )

        return logging.getLogger(__name__)
