from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    FRONTEND_NAME = ""  # Name in the config file

    registry = {}

    def __init__(self, *, settings: dict):
        try:
            self.settings = settings[self.FRONTEND_NAME]
        except KeyError:
            raise AttributeError(
                f"Did not override variable FRONTEND_NAME "
                f"in subclass {self.__class__.__name__}"
            )

    @abstractmethod
    def display(self, message):
        """Display the message in the format provided by the class"""
        return NotImplemented
