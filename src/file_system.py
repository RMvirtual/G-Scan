import os
from pathlib import Path


def root_directory() -> Path:
    if "GSCAN_ROOT" in os.environ:
        return Path(os.environ["GSCAN_ROOT"])
    
    return Path(__file__).parent.parent


def image_resources_directory() -> Path:
    return root_directory().joinpath("data", "images")


def config_directory() -> Path:
    return root_directory().joinpath("config")


def user_settings_path() -> Path:
    return config_directory().joinpath("user_settings.json")
