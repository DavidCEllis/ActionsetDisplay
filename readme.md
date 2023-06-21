# Actionset Display #

In the latest Steam update Valve has managed to completely remove notifications
when changing controller actionsets.

For certain speedruns we generally use a toggle to switch between the sets
and rely on the prompt to know we have the correct controls. This tool attempts
to provide alternatives to the now non-working steam notifications.

Hopefully it will be fixed but this is not the first time these have been broken.

## How to use ##

**CURRENTLY THIS DOES NOT WORK FOR DUALSHOCK CONTROLLERS**

Make sure your controller is connected.
Modify config.toml to match your game settings and notification preferences.
Launch ActionsetDisplay.exe before launching the game.

## Adding a notifier ##

In order to create a new notifier you need to make a new python script in 
the src/steam_actionset_display/notifier/ folder with a class that inherits
from `BaseNotifier` and provides a `display` method that accepts the actionset
name for display and sets `FRONTEND_NAME` to the filename without the extension.

Then you need to modify `config.toml` to add `[notifier.<your_notifier>]` where
<your_notifier> is the name of the `.py` file.

Add `use_frontend = true` for it to be used automatically.


## Direct Dependencies ##

* Controller Inputs: [XInput-Python](https://github.com/Zuzu-Typ/XInput-Python)
* TTS: [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
* Windows Notifications: [windows-toasts](https://github.com/DatGuy1/Windows-Toasts)
* Process Detection: [psutil](https://github.com/giampaolo/psutil)
