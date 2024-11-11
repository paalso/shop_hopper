from abc import ABC, abstractmethod


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
