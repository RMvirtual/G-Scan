import os

import wx

import file_system
from configuration import Configuration
from controllers.editor.editor import EditorController
from database import JSONDatabase, JSONDatabaseFiles
from gui.window import Window


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
    display_width, display_height = wx.DisplaySize()
    size = (int(display_width / 2), int(display_height / 1.1))
    window = Window(size, position=wx.Point(size[0], 0))
    window.Show()
    EditorController(configuration, window)
    gui_runtime.MainLoop()


if __name__ == "__main__":
    main()
