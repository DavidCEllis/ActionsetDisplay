from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    """
    Base class for all notifiers

    This is used to find notifiers via __subclasses__

    Module detection is based on the config.toml
    Notifier detection is then based around subclassing this.
    """
    FRONTEND_NAME = ""  # Name in the config file

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
