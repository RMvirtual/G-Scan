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

    def launch_main_menu(self, event = None) -> None:
        self.display(self._create_main_menu())

    def launch_image_viewer(self, event = None) -> None:
        self.display(self._create_image_viewer())

    def launch_settings(self, event = None) -> None:
        self.display(self._create_settings())

    def show(self) -> None:
        self._window.show()

    def close(self, event = None) -> None:
        self._window.close()

    def save_settings(self, event = None) -> None:
        self.launch_main_menu()

    def display(self, controller: DisplayController) -> None:
        if self.active_controller:
            self.active_controller.close()

        self.active_controller = controller
        self._window.display(self.active_controller)

    def _create_main_menu(self) -> DisplayController:
        result = MainMenuController(self._window)

        result.bind_customer_paperwork(self.launch_image_viewer)
        result.bind_loading_list(self.launch_image_viewer)
        result.bind_settings(self.launch_settings)
        result.bind_exit(self.close)

        return result

    def _create_image_viewer(self) -> DisplayController:
        result = ImageViewerController(self._window)
        result.bind_exit(self.launch_main_menu)

        return result

    def _create_settings(self) -> DisplayController:
        result = SettingsController(self._window)
        result.bind_save_button(self.save_settings)
        result.bind_exit_button(self.launch_main_menu)

        return result