from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.settings import SettingsController
from src.main.gui.window import Window


class ApplicationController:
    def __init__(self):
        self._initialise_window()
        self.active_controller = None

    def _initialise_window(self) -> None:
        self._window = Window()
        self._window.Show()

    def launch_main_menu(self) -> None:
        if self.active_controller:
            self.active_controller.close()

        main_menu = MainMenuController(self._window)
        main_menu.bind_customer_paperwork(self.launch_image_viewer)
        main_menu.bind_loading_list(self.launch_image_viewer)
        main_menu.bind_settings(self.launch_settings)
        main_menu.bind_exit(self.close)

        self._window.panel = main_menu.panel
        main_menu.show()
        self.active_controller = main_menu

    def launch_image_viewer(self, event = None) -> None:
        if self.active_controller:
            self.active_controller.close()

        image_viewer = ImageViewerController(self._window)
        self._window.panel = image_viewer.panel
        image_viewer.show()
        self.active_controller = image_viewer

    def launch_settings(self, event = None) -> None:
        if self.active_controller:
            self.active_controller.close()

        image_viewer = SettingsController(self._window)
        self._window.panel = image_viewer.panel
        image_viewer.show()
        self.active_controller = image_viewer

    def close(self, event = None) -> None:
        self._window.Close()
