import os

import wx

import file_system
from configuration import Configuration
from controllers.editor import EditorController
from database import JSONDatabase, JSONDatabaseFiles


def main() -> None:
    config_directory = file_system.data_directory()

    database_files = list(
        map(
            config_directory.joinpath,
            ["departments.json", "document_types.json", "user_settings.json"],
        )
    )

    database = JSONDatabase(JSONDatabaseFiles(*database_files))
    configuration = Configuration(database, os.getlogin())
    gui_runtime = wx.App()
    EditorController(configuration)
    gui_runtime.MainLoop()


if __name__ == "__main__":
    main()
