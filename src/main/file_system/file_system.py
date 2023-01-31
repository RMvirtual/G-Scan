import os
from src.main.file_system import runfiles


def user_settings_path():
    return app_data_directory() + "\\user_settings.json"


def app_data_directory():
    return os.environ["LOCALAPPDATA"] + "\\G-Scan"


def config_directory() -> str:
    return runfiles.runfile_path("config")


def image_resources_directory() -> str:
    return runfiles.runfile_path("resources\\images")


def test_resources_directory() -> str:
    return runfiles.runfile_path("resources\\test")
