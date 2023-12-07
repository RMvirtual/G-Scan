import wx
from app.configuration import ViewerConfiguration
from app.controllers.main_menu import MainMenuController
from app.controllers.viewer.application import ViewerApplicationController
from app.controllers.settings import SettingsController
from app.interfaces import RootInterface
from gui.window import Window


class RootApplication(RootInterface):
    def __init__(self):
        self._window = Window()

    def launch_main_menu(self) -> None:
        MainMenuController(root_application=self)

    def launch_settings(self) -> None:
        SettingsController(root_application=self)

    def launch_image_viewer(self, config: ViewerConfiguration) -> None:
        ViewerApplicationController(root_application=self, config=config)

    @property
    def window(self) -> Window:
        return self._window

    def show(self) -> None:
        self._window.Show()

    def close(self, event = None) -> None:
        self._window.Close()

    def exit(self) -> None:
        self.close()
