from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.settings import SettingsController
from src.main.app.controllers.window import WindowController
from src.main.app.controllers.display_interface import DisplayController

class ApplicationController:
    def __init__(self):
        self._initialise_window()
        self.active_controller = None

    def _initialise_window(self) -> None:
        self._window = WindowController()
        self._window.show()

    def launch_main_menu(self, event = None) -> None:
        main_menu = MainMenuController(self._window)
        main_menu.bind_customer_paperwork(self.launch_image_viewer)
        main_menu.bind_loading_list(self.launch_image_viewer)
        main_menu.bind_settings(self.launch_settings)
        main_menu.bind_exit(self.close)

        self.display(main_menu)

    def launch_image_viewer(self, event = None) -> None:
        image_viewer = ImageViewerController(self._window)
        image_viewer.bind_exit(self.launch_main_menu)

        self.display(image_viewer)

    def launch_settings(self, event = None) -> None:
        settings = SettingsController(self._window)
        settings.bind_save_button(self.save_settings)
        settings.bind_exit_button(self.launch_main_menu)

        self.display(settings)

    def close(self, event = None) -> None:
        self._window.close()

    def save_settings(self, event = None) -> None:
        self.launch_main_menu()

    def display(self, controller: DisplayController) -> None:
        if self.active_controller:
            self.active_controller.close()

        self.active_controller = controller
        self._window.display(self.active_controller)
