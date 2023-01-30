from abc import ABC, abstractmethod
from src.main.app.display import Display


class SettingsInterface(Display):
    @abstractmethod
    def launch_main_menu(self) -> None:
        ...


