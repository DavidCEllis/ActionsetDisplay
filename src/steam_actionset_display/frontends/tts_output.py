"""
Text to Speech output mode using pyttsx3
"""
import pyttsx3
from concurrent.futures import ThreadPoolExecutor


class Speaker:
    """
    Setup a thread for the speaker so it won't block multiple inputs
    but it will announce each button press.
    """
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=1)

    def display(self, message):
        _ = self.pool.submit(self._speak, message)

    @staticmethod
    def _speak(message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()


def main():
    speaker = Speaker()
    speaker.display("Prompt Swap")
    speaker.display("Default")
    print("Messages Sent")


if __name__ == "__main__":
    main()
