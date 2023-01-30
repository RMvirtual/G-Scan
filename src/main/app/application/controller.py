import wx
from src.main.app.image_viewer.controller import ImageViewerController
from src.main.app.settings.controller import SettingsController
from src.main.app.display import DisplayController, Display
from src.main.app.main_menu import RootMenu, MainMenuController
from src.main.app.application.interface import ApplicationInterface


class ApplicationController(ApplicationInterface):
    def __init__(self):
        self._display = DisplayController()
        self._active_controller = None

    def launch_main_menu(self, event = None) -> None:
        self._set_controller(
            MainMenuController(application=self))

        self._display.frame().Layout()

    def launch_image_viewer(self, event = None) -> None:
        self._clear_controller()

        self._active_controller = ImageViewerController(self._display)

    def launch_settings(self, event = None) -> None:
        self._clear_controller()

        self._active_controller = SettingsController(self._display)

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
        self._active_controller = controller

    def _clear_controller(self) -> None:
        if self._active_controller:
            self._active_controller.close()

    def _create_image_viewer(self) -> None:
        # result.bind_exit(self.launch_main_menu)

        # return result
        ...

    def _create_settings(self) -> None:
        # result.bind_save_button(self.save_settings)
        # result.bind_exit_button(self.launch_main_menu)

        # return result
        ...