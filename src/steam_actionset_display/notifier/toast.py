"""
Windows notification output mode using plyer
"""

import plyer
from .base import BaseNotifier
from ..data import icon_file

APP_NAME = "ActionSet Display"
APP_ICON = icon_file


class ToastNotifier(BaseNotifier):
    FRONTEND_NAME = "toast"

    def display(self, message):
        plyer.notification.notify(
            title=self.settings['title'],
            message=message,
            app_name=APP_NAME,
            app_icon=str(icon_file)
        )


def main():
    import time
    plyer.notification.notify(
        title="Test Title",
        message="Test Message",
        app_name=APP_NAME,
        app_icon=str(icon_file),
    )

    time.sleep(1)

    plyer.notification.notify(
        title="Test Title",
        message="Test Message 2",
        app_name=APP_NAME,
        app_icon=str(icon_file),
    )

    time.sleep(1)

    plyer.notification.notify(
        title="Test Title",
        message="Test Message 3",
        app_name=APP_NAME,
        app_icon=str(icon_file),
    )


if __name__ == "__main__":
    main()
