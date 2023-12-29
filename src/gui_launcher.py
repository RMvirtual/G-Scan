import os
import wx
import file_system

from app.configuration import AppConfiguration
from app.main_menu import MainMenuController
from app.viewer import ViewerApplicationController
from app.settings import SettingsController
from app.abstract_root import RootInterface
from gui.window import Window
from database import JSONDatabase
from file_system import JSONDatabaseFiles


class RootApplication(RootInterface):
    def __init__(self, database: JSONDatabase, app_config: AppConfiguration):
        self.window = Window()
        self._database = database
        self._config = app_config

    def launch_main_menu(self) -> None:
        MainMenuController(self, self._config)

    def launch_settings(self) -> None:
        SettingsController(self, self._config)

    def launch_image_viewer(self, config: AppConfiguration) -> None:
        ViewerApplicationController(self, config)

    def show(self) -> None:
        self.window.Show()

    def close(self, event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()


def main() -> None:
    """Default entry point using current OS username logged in."""

    gui_runtime = wx.App()
    
    database = _default_database()
    app_config = AppConfiguration(database, os.getlogin())

    controller = RootApplication(database, app_config)
    controller.show()
    controller.launch_main_menu()
    
    gui_runtime.MainLoop()


def _default_database() -> JSONDatabase:
    database_files = [
        "departments.json", "document_types.json", "user_settings.json"]

    config_dir = file_system.config_directory()   
    file_paths = list(map(config_dir.joinpath, database_files))

    return JSONDatabase(JSONDatabaseFiles(*file_paths))


if __name__ == '__main__':
    main()
    