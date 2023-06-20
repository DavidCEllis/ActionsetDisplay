import XInput as xinput

FILTERS = {
    "DPAD_UP": xinput.BUTTON_DPAD_UP,
    "DPAD_DOWN": xinput.BUTTON_DPAD_DOWN,
    "DPAD_LEFT": xinput.BUTTON_DPAD_LEFT,
    "DPAD_RIGHT": xinput.BUTTON_DPAD_RIGHT,
    "START": xinput.BUTTON_START,
    "BACK": xinput.BUTTON_BACK,
    "LEFT_THUMB": xinput.BUTTON_LEFT_THUMB,
    "RIGHT_THUMB": xinput.BUTTON_RIGHT_THUMB,
    "LEFT_SHOULDER": xinput.BUTTON_LEFT_SHOULDER,
    "RIGHT_SHOULDER": xinput.BUTTON_RIGHT_SHOULDER,
    "A": xinput.BUTTON_A,
    "B": xinput.BUTTON_B,
    "X": xinput.BUTTON_X,
    "Y": xinput.BUTTON_Y,
}


class ButtonHandler(xinput.EventHandler):
    def __init__(
            self,
            *controllers,
            callback_func,
            filter=xinput.FILTER_NONE,
    ):
        super().__init__(*controllers, filter=filter)
        self.callback_func = callback_func

    def process_button_event(self, event):
        if event.type == 3:  # Down Press
            self.callback_func()

    def process_trigger_event(self, event):
        pass

    def process_stick_event(self, event):
        pass

    def process_connection_event(self, event):
        pass
