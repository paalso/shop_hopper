from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def save(self, data, query, logger, path='.'):
        pass
