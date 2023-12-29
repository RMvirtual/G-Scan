from app.root_interface import RootInterface
from configuration import Configuration
from controllers.document_editor import DocumentEditorController
from controllers.main_menu import MainMenuController
from controllers.settings import SettingsController
from views.window import Window


class RootApplication(RootInterface):
    def __init__(self, app_config: Configuration):
        self.window = Window()
        self._config = app_config

    def launch_main_menu(self) -> None:
        MainMenuController(self, self._config, self.window)

    def launch_settings(self) -> None:
        SettingsController(self, self._config, self.window)

    def launch_image_viewer(self, config: Configuration) -> None:
        DocumentEditorController(self, config, self.window)

    def show(self) -> None:
        self.window.Show()

    def close(self, event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()
