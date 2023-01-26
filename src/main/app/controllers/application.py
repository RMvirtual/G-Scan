from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController

class ApplicationController:
    def __init__(self):
        self._main_menu = MainMenuController()

    def launch_main_menu(self) -> None:
        self._main_menu.launch()
