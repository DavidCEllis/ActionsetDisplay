"""
Windows notification output mode using plyer
"""

import plyer
from pathlib import Path

APP_NAME = "ActionSet Display"
APP_ICON = Path(__file__).parent / "game-controller.ico"


class ToastNotifier:
    def __init__(self, *, timeout=1):
        self.timeout = timeout

    def display(self, message):
        plyer.notification.notify(
            title="Action Set Changed",
            message=message,
            app_name=APP_NAME,
            app_icon=str(APP_ICON),
            timeout=self.timeout
        )


def main():
    import time
    plyer.notification.notify(
        title="Test Title",
        message="Test Message",
        app_name=APP_NAME,
        app_icon=str(APP_ICON),
    )

    time.sleep(1)

    plyer.notification.notify(
        title="Test Title",
        message="Test Message 2",
        app_name=APP_NAME,
        app_icon=str(APP_ICON),
    )

    time.sleep(1)

    plyer.notification.notify(
        title="Test Title",
        message="Test Message 3",
        app_name=APP_NAME,
        app_icon=str(APP_ICON),
    )


if __name__ == "__main__":
    main()
