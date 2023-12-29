import wx
import database

from app.abstract_root import RootInterface
from app.configuration import AppConfiguration
from gui import Settings
from user import UserSettings


class SettingsController:
    def __init__(
            self, root_application: RootInterface, app_config: AppConfiguration
    ) -> None:
        self._root = root_application
        self._config = app_config

        self._gui = Settings(self._root.window)
        self._root.window.set_panel(self._gui)

        self._gui.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._gui.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._gui.directories.scan_browse.Bind(
            wx.EVT_BUTTON, self.on_scan_dir_browse)
        
        self._gui.directories.dest_browse.Bind(
            wx.EVT_BUTTON, self.on_dest_dir_browse)

        self._gui.defaults.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_box)

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._load_settings_from_file()

    def on_save(self, event = None) -> None:
        new_settings = self._settings_from_gui()
        
        self._config.database.save_user_settings(new_settings)
        self._config.settings = new_settings

        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_scan_dir_browse(self, event = None) -> None:
        user_selection = self._directory_dialog()

        if user_selection:
            self._gui.directories.scan_directory = user_selection

    def on_dest_dir_browse(self, event = None) -> None:
        user_selection = self._directory_dialog()

        if user_selection:
            self._gui.directories.dest_directory = user_selection

    def on_department_box(self, event = None) -> None:
        self._refresh_document_options()

    def on_close(self, event = None) -> None:
        self._gui.Destroy()

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

    def _load_settings_from_file(self) -> None:
        settings = self._config.settings

        self._gui.directories.scan_directory = settings.scan_dir
        self._gui.directories.dest_directory = settings.dest_dir

        department_names = list(map(
            lambda dept: dept.full_name, 
            self._config.database.all_departments()
        ))
        
        self._gui.defaults.department_options = department_names
        self._gui.defaults.department = settings.department.full_name

        document_names = list(map(
            lambda d: d.full_name, settings.department.document_types))

        self._gui.defaults.document_options = document_names
        self._gui.defaults.document_type = settings.document_type.full_name

        self._root.window.Layout()

    def _refresh_document_options(self) -> None:
        department_name = self._gui.defaults.department
        department = self._config.database.department(full_name=department_name)

        document_names = list(map(
            lambda document: document.full_name, department.document_types))

        # document_names = department.document_types.full_names()

        self._gui.defaults.document_options = document_names
        self._gui.defaults.document_type = document_names[0]

    def _settings_from_gui(self) -> UserSettings:
        result = UserSettings()

        result.scan_dir = self._gui.directories.scan_directory
        result.dest_dir = self._gui.directories.dest_directory

        result.department = self._config.database.department(
            full_name=self._gui.defaults.department)

        result.document_type = self._config.database.document(
            full_name=self._gui.defaults.document_type)

        return result

    @staticmethod
    def _directory_dialog() -> str or None:
        with wx.DirDialog(None) as browser:
            return (
                None if browser.ShowModal() == wx.ID_CANCEL
                else browser.GetPath()
            )
