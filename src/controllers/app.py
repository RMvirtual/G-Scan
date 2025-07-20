import os

import wx

import file_system
from configuration import Configuration
from controllers.editor.editor import EditorController
from controllers.mediator import ApplicationMediator
from controllers.settings import SettingsDialogController
from database import JSONDatabase, JSONDatabaseFiles, UserSettings
from gui.window import Window


class MainApplication(ApplicationMediator):
    def __init__(self, config: Configuration):
        display_width, display_height = wx.DisplaySize()
        size = (int(display_width / 2), int(display_height / 1.1))

        self.window = Window(size, position=wx.Point(size[0], 0))
        self.config = config

    def launch_editor(self) -> None:
        EditorController(self, self.config, self.window)

    def launch_settings(self) -> None:
        department_options = self.config.database.all_departments()
        user_settings = self.config.settings

        settings_controller = SettingsDialogController(
            self, self.window, department_options, user_settings
        )

        self.window.set_panel(settings_controller.gui)

    def update_user_settings(self, settings: UserSettings) -> None:
        database = self.config.database
        database.save_user_settings(settings)
        self.config.settings = settings

    def show(self) -> None:
        self.window.Show()

    def close(self, event: wx.Event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()


def main() -> None:
    gui_runtime = wx.App()
    config_directory = file_system.data_directory()

    database_files = list(
        map(
            config_directory.joinpath,
            ["departments.json", "document_types.json", "user_settings.json"],
        )
    )

    database = JSONDatabase(JSONDatabaseFiles(*database_files))
    configuration = Configuration(database, os.getlogin())

    controller = MainApplication(configuration)
    controller.show()
    controller.launch_editor()

    gui_runtime.MainLoop()


if __name__ == "__main__":
    main()
