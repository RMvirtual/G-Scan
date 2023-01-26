from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController


class ApplicationController:
    def __init__(self):
        self._main_menu = MainMenuController()
        self._image_viewer = ImageViewerController()
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._main_menu.bind_customer_paperwork(self.show_image_viewer)
        self._main_menu.bind_loading_list(self.show_image_viewer)
        self._main_menu.bind_exit(self.exit)

        self._image_viewer.bind_exit(self.show_main_menu)

    def show_main_menu(self, event = None) -> None:
        self._image_viewer.hide()
        self._main_menu.show()

    def show_image_viewer(self, event = None) -> None:
        self._main_menu.hide()
        self._image_viewer.show()

    def exit(self, event = None) -> None:
        self._main_menu.close()
        self._image_viewer.close()
