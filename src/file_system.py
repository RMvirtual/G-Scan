import os
import sys
from pathlib import Path


def root_directory() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    if "GSCAN_ROOT" in os.environ:
        return Path(os.environ["GSCAN_ROOT"])
    
    raise ValueError(
        "Cannot determine root directory from either the Pyinstaller "
        "sys._MEIPASS variable or the GSCAN_ROOT environment variable."
    )


def image_resources_directory() -> Path:
    return root_directory().joinpath("data", "images")


def data_directory() -> Path:
    return root_directory().joinpath("data")


def user_settings_path() -> Path:
    return data_directory().joinpath("user_settings.json")
