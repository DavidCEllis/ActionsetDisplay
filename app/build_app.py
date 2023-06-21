# Build the application
import PyInstaller.__main__ as pyinstaller
from pathlib import Path
import shutil

project_folder = Path(__file__).parents[1]

icon_file = project_folder / "src/steam_actionset_display/data/game-controller.ico"


def get_hiddenimports():
    import steam_actionset_display.notifier
    # Don't include the files that are already detected
    exclude_files = ["__init__", "base"]

    base_path = Path(steam_actionset_display.notifier.__file__).parent
    searcher = base_path.glob("*.py")

    hidden_import = "steam_actionset_display.notifier.{module}"

    imports = [
        hidden_import.format(module=f.stem)
        for f in searcher
        if f.stem not in exclude_files
    ]

    return imports


def copy_extras():
    """
    Copy over the config file and readme.
    """
    config_file = project_folder / "app" / "config.toml"
    readme_file = project_folder / "readme.md"

    dest_folder = project_folder / "app" / "dist"

    shutil.copy(config_file, dest_folder)
    shutil.copy(readme_file, dest_folder)


def build_app():
    pyinstaller_args = [
        "app.py",
        "--name ActionsetDisplay",
        "--onefile",
        f"--add-data={icon_file};.",
        f"--icon={icon_file}"
    ]

    for module in get_hiddenimports():
        pyinstaller_args.append(
            f"--hidden-import={module}"
        )

    pyinstaller.run(pyinstaller_args)

    copy_extras()


if __name__ == "__main__":
    build_app()
