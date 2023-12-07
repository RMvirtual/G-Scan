import os
import json
import wx


def file_import_dialog() -> list[str]:
    browser_style = (wx.FD_MULTIPLE | wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    with wx.FileDialog(parent=None, style=browser_style) as browser:
        if browser.ShowModal() == wx.ID_CANCEL:
            return []

        return browser.GetPaths()


def load_json(path: str) -> dict[str, any]:
    with open(path, "r") as file_stream:
        return json.loads(file_stream.read())


def app_data_directory() -> str:
    """Local AppData path folder for G-Scan's root data folder."""

    return os.environ["LOCALAPPDATA"] + "\\G-Scan"


def user_settings_path() -> str:
    """Local AppData path for G-Scan's user settings json file."""

    return app_data_directory() + "\\user_settings.json"
