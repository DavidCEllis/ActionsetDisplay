from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    @abstractmethod
    def display(self, message):
        return NotImplemented

