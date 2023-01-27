from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.settings import SettingsController
from src.main.app.controllers.window import WindowController


class ApplicationController:
    def __init__(self):
        self._initialise_window()

    def _initialise_window(self) -> None:
        self._window_controller = WindowController()
        self._window_controller.show()
