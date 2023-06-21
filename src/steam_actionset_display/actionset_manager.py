import tomllib
import importlib
import itertools
import time

# noinspection PyPep8Naming
import XInput as xinput

from .exceptions import ApplicationError
from .notifier.base import BaseNotifier
from .process_detection import ProcessRunningCheck
from .input_reader import FILTERS, ButtonHandler


PACKAGE_NAME = "steam_actionset_display"


def make_callback(
        *,
        notifiers: list[BaseNotifier],
        game_detector: ProcessRunningCheck,
        actionset_list: list[str],
):
    """
    Get a function that will announce the current actionset to all notifiers
    if the game is running and reset the list if not.
    """
    actionset_loop = itertools.cycle(actionset_list)
    _ = next(actionset_loop)  # Skip the first value as that is the initial setting

    def callback():
        nonlocal actionset_loop

        # If the game has been restarted we need to reset the loop
        # The first attempt will say it is not running in this case
        if not game_detector.is_running():
            # Reset the loop
            actionset_loop = itertools.cycle(actionset_list)
            _ = next(actionset_loop)

        # Now check if the game is focused
        if game_detector.has_focus():

            message = next(actionset_loop)

            print(message)
            for notifier in notifiers:
                notifier.display(message)
        elif game_detector.is_running():
            print("Game is running but not in focus")
        else:
            print("Button pressed but game is not running")

    return callback


def run_application(config_path):
    # Get controllers
    controllers = xinput.get_connected()
    if not any(controllers):
        raise ApplicationError("No Controllers Detected")

    controller_id = controllers.index(True)

    # Read the config and get useful settings
    config_data = tomllib.loads(config_path.read_text())

    keypress_name = config_data["keypress"]
    exe_list = config_data["game_exes"]
    actionset_list = config_data["action_sets"]
    notifier_conf = config_data['notifier']

    # Attempt to get the actual keypress
    try:
        keypress = FILTERS[keypress_name]
    except KeyError:
        raise ValueError(
            f"Keypress: {keypress_name} is not a valid keypress."
            f"Pleaase check your config.toml keypress value"
        )

    # Import every notifier with use_frontend=True
    for module_name, settings in notifier_conf.items():
        if settings["use_frontend"]:
            importlib.import_module(f".notifier.{module_name}", PACKAGE_NAME)

    # Get the list of notifiers to use
    notifiers: list[BaseNotifier] = [
        cls(settings=notifier_conf) for cls in BaseNotifier.__subclasses__()
    ]

    # Get the game detection tool
    game_detector = ProcessRunningCheck(exe_list)

    callback = make_callback(
        notifiers=notifiers,
        game_detector=game_detector,
        actionset_list=actionset_list,
    )

    button_handler = ButtonHandler(
        controller_id,
        callback_func=callback,
        filter=keypress,
    )

    gamepad_thread = xinput.GamepadThread(button_handler)
    print("Started Detection.")
    print("Press ctrl+c to close application.")

    # Just sleep in the main thread
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Closing Application")
    finally:
        gamepad_thread.stop()

