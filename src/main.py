import os
import wx
import file_system

from configuration import Configuration
from controllers.root_application import RootApplication
from database import JSONDatabase
from file_system import JSONDatabaseFiles


def main() -> None:
    """Default entry point using current OS username logged in."""

    gui_runtime = wx.App()
    config_directory = file_system.config_directory()   
    
    database_files = list(map(
        config_directory.joinpath,
        ["departments.json", "document_types.json", "user_settings.json"]
    ))

    database = JSONDatabase(JSONDatabaseFiles(*database_files))
    configuration = Configuration(database, os.getlogin())

    controller = RootApplication(configuration)
    controller.show()
    controller.launch_main_menu()
    
    gui_runtime.MainLoop()


if __name__ == '__main__':
    main()
    