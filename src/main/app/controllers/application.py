from src.main.app.controllers.image_viewer import ImageViewerController
from src.main.app.controllers.main_menu import MainMenuController
from src.main.app.controllers.settings import SettingsController

class ApplicationController:
    def __init__(self):
        self._initialise_apps()
        self._active_app = self._main_menu

    def _initialise_apps(self) -> None:
        self._main_menu = MainMenuController()
        self._image_viewer = ImageViewerController()
        self._settings = SettingsController()
        self._apps = [
            self._main_menu, self._image_viewer, self._settings]

        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._main_menu.bind_customer_paperwork(self.launch_image_viewer)
        self._main_menu.bind_loading_list(self.launch_image_viewer)

        self._main_menu.bind_settings(self.launch_settings)
        self._main_menu.bind_exit(self.close_all)

        self._settings.bind_save_button(self.launch_main_menu)
        self._settings.bind_exit_button(self.launch_main_menu)

        self._image_viewer.bind_exit(self.launch_main_menu)

    def launch_main_menu(self, event = None) -> None:
        self.switch_to(self._main_menu)

    def launch_image_viewer(self, event = None) -> None:
        self.switch_to(self._image_viewer)

    def launch_settings(self, event = None) -> None:
        self.switch_to(self._settings)

    def close_all(self, event = None) -> None:
        for app in self._apps:
            app.close()

    def switch_to(self, application) -> None:
        self._active_app.hide()
        self._active_app = application

        self._active_app.show()
