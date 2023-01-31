import json
import wx
from src.main import file_system
from src.main.app.root.interface import RootInterface
from src.main.gui import Settings
from src.main import user
from src.main import departments, documents

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
        settings = user.get_settings()

        self._set_directories(settings)
        self._set_department(settings)
        self._set_document_type(settings)

    def _set_directories(self, settings: user.UserSettings) -> None:
        self._gui.directories.scan_directory = settings.scan_dir
        self._gui.directories.dest_directory = settings.dest_dir

    def _set_department(self, settings: user.UserSettings) -> None:
        department_names = departments.load_all().full_names()
        self._gui.defaults.department_options = department_names
        self._gui.defaults.department = settings.department.full_name

    def _set_document_type(self, settings: user.UserSettings) -> None:
        document_names = settings.department.document_types.full_names()
        self._gui.defaults.document_options = document_names
        self._gui.defaults.document_type = settings.document_type.full_name

    def on_save(self, event = None) -> None:
        self._root.launch_main_menu()

    def on_exit(self,event = None) -> None:
        self._root.launch_main_menu()
