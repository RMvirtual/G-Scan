import json
import wx
from src.main import file_system
from src.main.app.root.interface import RootInterface
from src.main.gui import Settings
from src.main import user
from src.main import departments

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

        self._gui.directories.scan_directory = settings.scan_dir
        self._gui.directories.dest_directory = settings.dest_dir
        self._gui.defaults.department = settings.department.short_name
        self._gui.defaults.document_type = settings.document_type.full_name

        department_types = departments.load_all()

        stringly_departments = [
            department.short_name for department in department_types]

        self._gui.defaults.department_options = stringly_departments

        document_types = settings.department.document_types
        stringly_types = [document.full_name for document in document_types]

        self._gui.defaults.document_options = stringly_types

    def on_save(self, event = None) -> None:
        self._root.launch_main_menu()

    def on_exit(self,event = None) -> None:
        self._root.launch_main_menu()
