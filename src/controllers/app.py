import os
import wx

import file_system
from configuration import Configuration
from controllers.document_editor.editor import DocumentEditorController
from controllers.main_menu import MainMenuController
from controllers.settings import SettingsController
from controllers.selector import AppSelector
from database import JSONDatabase, JSONDatabaseFiles
from gui.window import Window


class MainApplication(AppSelector):
    def __init__(self, config: Configuration):
        display_width, display_height = wx.DisplaySize()
        size = (int(display_width/2), int(display_height/1.1))
        
        self.window = Window(size, position=wx.Point(size[0],0))
        self.config = config

    def launch_main_menu(self) -> None:
        MainMenuController(self, self.config, self.window)

    def launch_settings(self) -> None:
        SettingsController(self, self.config, self.window)

    def launch_image_viewer(self, config: Configuration) -> None:
        DocumentEditorController(self, config, self.window)

    def show(self) -> None:
        self.window.Show()

    def close(self, event: wx.Event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()


def main() -> None:
    gui_runtime = wx.App()
    config_directory = file_system.data_directory()   
    
    database_files = list(map(
        config_directory.joinpath,
        ["departments.json", "document_types.json", "user_settings.json"]
    ))

    database = JSONDatabase(JSONDatabaseFiles(*database_files))
    configuration = Configuration(database, os.getlogin())

    controller = MainApplication(configuration)
    controller.show()
    controller.launch_main_menu()
    
    gui_runtime.MainLoop()


if __name__ == '__main__':
    main()
    