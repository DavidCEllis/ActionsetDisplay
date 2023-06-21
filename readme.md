# Steam Actionset Display #

In the latest Steam update Valve has managed to completely remove notifications
when changing controller actionsets.

For certain speedruns we generally use a toggle to switch between the sets
and rely on the prompt to know we have the correct controls. This tool attempts
to provide alternatives to the now non-working steam notifications.

Hopefully it will be fixed but this is not the first time these have been broken.

## How to use ##

In this testing phase there isn't an .exe so you'll need to have python 3.11 
installed. Get that from python.org or directly here: 
[python.org](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)

You can modify the `config.toml` file in order to turn on and off notifiers
and change other settings.

There are two powershell scripts to help setup python for the application
and launch the application. (Right click - run with powershell).

setup_environment.ps1 is needed once for the initial setup and download of dependencies

launch_application.ps1 should be used to launch the app.


## Adding a notifier ##

In order to create a new notifier you need to make a new python script in 
the src/steam_actionset_display/notifier/ folder with a class that inherits
from `BaseNotifier` and provides a `display` method that accepts the actionset
name for display and sets `FRONTEND_NAME` to the filename without the extension.

Then you need to modify `config.toml` to add `[notifier.<your_notifier>]` where
<your_notifier> is the name of the `.py` file.

Add `use_frontend = true` for it to be used automatically.
