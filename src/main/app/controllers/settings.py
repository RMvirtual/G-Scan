import json
import wx
from src.main.app.root.interface import RootInterface
from src.main.gui import Settings
from src.main.file_system.runfiles import config_directory


class SettingsController:
    def __init__(self, root_application: RootInterface):
        self._root = root_application
        self._gui = Settings(root_application.frame())
        self._initialise_callbacks()
        self.load_directories()

    def _initialise_callbacks(self) -> None:
        self._gui.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._gui.exit.Bind(wx.EVT_BUTTON, self.on_exit)

    def close(self) -> None:
        self._gui.close()

    @property
    def panel(self) -> wx.Panel:
        return self._gui

    def load_directories(self) -> None:
        user_exists = False

        if not user_exists:
            directory = config_directory()

            with open(directory + "\\user_defaults.json", "r") as _file:
                contents = json.loads(_file.read())

        self._gui.directories.scan_directory = (
            "NULL" if not contents["scan_directory"]
            else contents["scan_directory"]
        )

        self._gui.directories.dest_directory = contents["dest_directory"]


    def on_save(self, event = None) -> None:
        self._root.launch_main_menu()

    def on_exit(self,event = None) -> None:
        self._root.launch_main_menu()
