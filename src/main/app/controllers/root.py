import wx
from src.main.app.configurations import ImageViewerConfiguration
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.viewer import ImageViewerController
from src.main.app.controllers.settings import SettingsController
from src.main.app.controllers.window import DisplayController
from src.main.app.interfaces import RootInterface
from src.main.gui.window import Window


class RootApplication(RootInterface):
    def __init__(self):
        self._display = DisplayController()
        self._controller = None

    def launch_main_menu(self) -> None:
        self._set_controller(
            MainMenuController(root_application=self))

    def launch_settings(self) -> None:
        self._set_controller(
            SettingsController(root_application=self))

    def launch_image_viewer(self, config: ImageViewerConfiguration) -> None:
        self._set_controller(
            ImageViewerController(root_application=self, configuration=config))

    @property
    def window(self) -> Window:
        return self._display.window

    def show(self) -> None:
        self._display.show()

    def close(self, event = None) -> None:
        self._display.close()

    def exit(self) -> None:
        self.close()

    def _set_controller(self, controller) -> None:
        if self._controller:
            self._controller.close()

        self._controller = controller
        self.set_panel(self._controller.panel)

        self._display.window.Layout()
