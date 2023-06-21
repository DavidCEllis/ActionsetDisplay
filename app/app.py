import sys
from pathlib import Path

from steam_actionset_display.actionset_manager import run_application

if getattr(sys, "frozen", False):
    base_path = Path(sys.executable).parent
else:
    base_path = Path(__file__).parent

config_path = base_path / "config.toml"

try:
    run_application(config_path)
except Exception as e:
    print(f"An exception occured and the program is closing: {type(e).__name__} - {e}")
    input("Press Enter to close...")
