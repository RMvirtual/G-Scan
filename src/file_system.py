import json
import wx

from pathlib import Path


def file_import_dialog() -> list[str]:
    browser_style = (wx.FD_MULTIPLE | wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    with wx.FileDialog(parent=None, style=browser_style) as browser:
        if browser.ShowModal() == wx.ID_CANCEL:
            return []

        return browser.GetPaths()


def load_json(path: str) -> any:
    with open(path, "r") as file_stream:
        return json.loads(file_stream.read())


def root_directory() -> Path:
    """Assumes structure of gscan/bin/file_system.py"""

    return Path(__file__).parent.parent


def image_resources_directory() -> Path:
    return root_directory().joinpath("resources", "images")


def config_directory() -> Path:
    return root_directory().joinpath("config")


def user_settings_path() -> Path:
    return config_directory().joinpath("user_settings.json")
