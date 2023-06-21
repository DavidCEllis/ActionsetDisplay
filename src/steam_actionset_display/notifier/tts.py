"""
Text to Speech output mode using pyttsx3
"""
import pyttsx3
from concurrent.futures import ThreadPoolExecutor

from .base import BaseNotifier


class TTSNotifier(BaseNotifier):
    """
    Text to speech notifier
    """
    FRONTEND_NAME = "tts"

    def __init__(self, *, settings: dict):
        super().__init__(settings=settings)
        # Setup a thread for the speaker so it won't block multiple inputs
        # but it will announce each button press.
        self.pool = ThreadPoolExecutor(max_workers=1)

    def display(self, message):
        _ = self.pool.submit(self._speak, message)

    def _speak(self, message):
        properties: dict = self.settings.get("property", {})

        engine = pyttsx3.init()
        for key, value in properties.items():
            engine.setProperty(key, value)
        engine.say(message)
        engine.runAndWait()


def main():
    speaker = TTSNotifier(settings={})
    speaker.display("Prompt Swap")
    speaker.display("Default")
    print("Messages Sent")


if __name__ == "__main__":
    main()
