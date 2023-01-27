from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.settings import SettingsController
from src.main.app.controllers.window import WindowController


class ApplicationController:
    def __init__(self):
        self._initialise_window()
        self.active_controller = None

    def _initialise_window(self) -> None:
        self._window_controller = WindowController()
        self._window_controller.show()

    def launch_main_menu(self) -> None:
        self.active_controller = MainMenuController(
            self._window_controller.window)

        self._window_controller.set_panel(self.active_controller.panel)
        self.active_controller.show()
        self._window_controller.refresh()
