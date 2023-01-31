import json
import wx
from src.main import file_system
from src.main.app.root.interface import RootInterface
from src.main.gui import Settings


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
        with open(file_system.user_settings_path(), "r") as user_settings:
            contents = json.loads(user_settings.read())

        self._gui.directories.scan_directory = (
            "NULL" if not contents["scan_directory"]
            else contents["scan_directory"]
        )

        self._gui.directories.dest_directory = contents["dest_directory"]


    def on_save(self, event = None) -> None:
        self._root.launch_main_menu()

    def on_exit(self,event = None) -> None:
        self._root.launch_main_menu()
