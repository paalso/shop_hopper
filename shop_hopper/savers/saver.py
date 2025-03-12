from abc import ABC, abstractmethod
from datetime import datetime
import os


class Saver(ABC):
    """
    Abstract base class for saving data.

    Child classes must implement the `save()` method to handle saving data
    in a specific format (e.g., CSV, JSON, database).
    """

    @abstractmethod
    def save(self, data, query, logger, path='.'):
        """
        Saves the data to a file or other destination, defined by the subclass.

        Should be implemented in the subclass.

        Args:
            data (list[dict]): The data to be saved (a list of dictionaries).
            query (str): The query string used to fetch the data.
            logger (Logger): An instance of a logger for logging the process.
            path (str, optional): The directory path where to save the data .
                                  Defaults to the current directory ('.').
        """
        pass

    def _build_file_path(self, query, output_dir, file_extension):
        """Generates the full path to save the file based
           on the request and the current date."""
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
        filename = \
            f"{'_'.join(query.lower().split())}_{timestamp}.{file_extension}"
        return os.path.join(output_dir, filename)
