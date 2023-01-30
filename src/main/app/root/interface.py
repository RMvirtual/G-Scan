from abc import ABC
from src.main.app.main_menu import RootMenu
from src.main.app.settings.interface import SettingsInterface


class ApplicationInterface(RootMenu, SettingsInterface):
    ...