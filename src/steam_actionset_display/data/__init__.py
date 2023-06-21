import sys
from pathlib import Path

__all__ = ["icon_file"]

try:
    base_path = Path(getattr(sys, "_MEIPASS"))  # pyinstaller folder
except AttributeError:
    base_path = Path(__file__).parent

icon_file = base_path / "game-controller.ico"
