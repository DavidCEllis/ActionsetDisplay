import sys
from pathlib import Path

__all__ = ["icon_file"]

if getattr(sys, "frozen", False):
    base_path = Path(sys.executable).parent
else:
    base_path = Path(__file__).parent

icon_file = base_path / "game-controller.ico"
