from pathlib import Path


def root_directory() -> Path:
    """Assumes structure of gscan/bin/file_system.py"""

    return Path(__file__).parent.parent


def image_resources_directory() -> Path:
    return root_directory().joinpath("resources", "images")


def config_directory() -> Path:
    return root_directory().joinpath("config")


def user_settings_path() -> Path:
    return config_directory().joinpath("user_settings.json")
