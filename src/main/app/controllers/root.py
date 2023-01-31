import wx
from src.main.app.configurations import ImageViewerConfiguration
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.settings import SettingsController
from src.main.app.controllers.display import DisplayController
from src.main.app.interfaces import RootInterface

class RootApplication(RootInterface):
    def __init__(self):
        self._display = DisplayController()
        self._controller = None

    def launch_main_menu(self) -> None:
        self._set_controller(MainMenuController(root_application=self))

    def launch_settings(self) -> None:
        self._set_controller(SettingsController(root_application=self))

    def launch_image_viewer(self, config: ImageViewerConfiguration) -> None:
        self._set_controller(
            ImageViewerController(root_application=self, configuration=config))

    def exit(self) -> None:
        self.close()

    def frame(self) -> wx.Frame:
        return self._display.frame()

    def show(self) -> None:
        self._display.show()

    def close(self, event = None) -> None:
        self._display.close()

    def _set_controller(self, controller) -> None:
        self._close_controller()
        self._controller = controller
        self._refresh_panel()
        self._display.frame().Layout()

    def _close_controller(self) -> None:
        if self._controller:
            self._controller.close()

    def _refresh_panel(self) -> None:
        self.set_panel(self._controller.panel)

    def set_panel(self, panel: wx.Panel) -> None:
        self._display.set_panel(panel)
