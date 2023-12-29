import os
import wx
import file_system

from configuration import AppConfiguration, RootInterface
from controllers.document_editor import DocumentEditorController
from controllers.main_menu import MainMenuController
from controllers.settings import SettingsController
from database import JSONDatabase
from file_system import JSONDatabaseFiles
from views.window import Window


class RootApplication(RootInterface):
    def __init__(self, app_config: AppConfiguration):
        self.window = Window()
        self._config = app_config

    def launch_main_menu(self) -> None:
        MainMenuController(self, self._config, self.window)

    def launch_settings(self) -> None:
        SettingsController(self, self._config, self.window)

    def launch_image_viewer(self, config: AppConfiguration) -> None:
        DocumentEditorController(self, config, self.window)

    def show(self) -> None:
        self.window.Show()

    def close(self, event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()


def main() -> None:
    """Default entry point using current OS username logged in."""

    gui_runtime = wx.App()
    config_directory = file_system.config_directory()   
    
    database_files = list(map(
        config_directory.joinpath,
        ["departments.json", "document_types.json", "user_settings.json"]
    ))

    database = JSONDatabase(JSONDatabaseFiles(*database_files))
    configuration = AppConfiguration(database, os.getlogin())

    controller = RootApplication(configuration)
    controller.show()
    controller.launch_main_menu()
    
    gui_runtime.MainLoop()



if __name__ == '__main__':
    main()
    