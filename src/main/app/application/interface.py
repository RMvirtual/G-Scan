from abc import ABC
from src.main.app.main_menu import RootMenu
from src.main.app.display import Display


class ApplicationInterface(RootMenu, Display):
    ...