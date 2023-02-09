import os
from src.main.file_system import runfiles


def app_data_directory() -> str:
    """Local AppData path folder for G-Scan's root data folder."""

    return os.environ["LOCALAPPDATA"] + "\\G-Scan"


def user_settings_path() -> str:
    """Local AppData path for G-Scan's user settings json file."""

    return app_data_directory() + "\\user_settings.json"


def config_directory() -> str:
    return runfiles.runfile_path("config")


def departments_path() -> str:
    return config_directory() + "\\departments.json"


def document_types_path() -> str:
    return config_directory() + "\\document_types.json"


def resources_directory() -> str:
    return runfiles.runfile_path("resources")


def image_resources_directory() -> str:
    return runfiles.runfile_path("resources\\images")

