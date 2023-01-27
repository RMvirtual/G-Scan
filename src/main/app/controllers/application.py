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
        main_menu = MainMenuController(self._window_controller.window)
        main_menu.bind_customer_paperwork(self.launch_image_viewer)
        main_menu.bind_loading_list(self.launch_image_viewer)
        main_menu.bind_settings(self.launch_settings)
        main_menu.bind_exit(self.close)

        self._window_controller.set_panel(main_menu.panel)
        main_menu.show()
        self.active_controller = main_menu

    def launch_image_viewer(self, event = None) -> None:
        print("Image Viewer launch.")

    def launch_settings(self, event = None) -> None:
        print("Settings launch.")

    def close(self, event = None) -> None:
        self._window_controller.close()
