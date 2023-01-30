import wx
from src.main.app.image_viewer.controller import ImageViewerController
from src.main.app.settings.controller import SettingsController
from src.main.app.display import DisplayController, Display
from src.main.app.main_menu import RootMenu, MainMenuController
from src.main.app.root.interface import ApplicationInterface


class RootApplication(ApplicationInterface):
    def __init__(self):
        self._display = DisplayController()
        self._controller = None

    def launch_main_menu(self, event = None) -> None:
        self._set_controller(MainMenuController(root_application=self))
        self._display.frame().Layout()

    def launch_settings(self, event = None) -> None:
        self._set_controller(SettingsController(root_application=self))
        self._display.frame().Layout()

    def launch_image_viewer(self, event = None) -> None:
        self._set_controller(ImageViewerController(self._display))
        self._display.frame().Layout()

    def exit(self) -> None:
        self.close()

    def frame(self) -> wx.Frame:
        return self._display.frame()

    def show(self) -> None:
        self._display.show()

    def close(self, event = None) -> None:
        self._display.close()

    def save_settings(self, event = None) -> None:
        self.launch_main_menu()

    def _set_controller(self, controller) -> None:
        self._clear_controller()
        self._controller = controller
        self._refresh_panel()

    def _clear_controller(self) -> None:
        if self._controller:
            self._controller.close()

    def _refresh_panel(self) -> None:
        self.set_panel(self._controller.panel)

    def set_panel(self, panel: wx.Panel) -> None:
        self._display.set_panel(panel)

    def _create_image_viewer(self) -> None:
        # result.bind_exit(self.launch_main_menu)

        # return result
        ...
