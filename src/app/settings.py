import wx
import database

from app.abstract_root import RootInterface
from app.configuration import AppConfiguration
from departments import Department
from gui import Settings
from user import UserSettings


class SettingsController:
    def __init__(
            self, root_application: RootInterface, app_config: AppConfiguration
    ) -> None:
        self._root = root_application
        self._config = app_config

        self._initialise_gui()
        self._initialise_callbacks()
        self._load_settings_from_file()

    def _initialise_gui(self) -> None:
        self._gui = Settings(self._root.window)
        self._root.window.set_panel(self._gui)

    def _initialise_callbacks(self) -> None:
        self._initialise_save_and_exit_callbacks()
        self._initialise_directory_callbacks()
        self._initialise_department_callbacks()

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

    def _initialise_save_and_exit_callbacks(self) -> None:
        self._gui.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._gui.exit.Bind(wx.EVT_BUTTON, self.on_exit)

    def _initialise_directory_callbacks(self) -> None:
        panel = self._gui.directories
        panel.scan_browse.Bind(wx.EVT_BUTTON, self.on_scan_dir_browse)
        panel.dest_browse.Bind(wx.EVT_BUTTON, self.on_dest_dir_browse)

    def _initialise_department_callbacks(self) -> None:
        panel = self._gui.defaults
        panel.department_box.Bind(wx.EVT_COMBOBOX, self.on_department_box)

    def on_save(self, event = None) -> None:
        database.save_user_settings(settings=self._settings_from_gui())
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
        self._set_from_user_settings(self._config.settings)
        self._root.window.Layout()

    def _refresh_document_options(self) -> None:
        department_name = self._gui.defaults.department
        department = database.load_department(full_name=department_name)
        self._set_document(department=department)

    def _set_from_user_settings(self, settings: UserSettings) -> None:
        self._set_directories(settings)
        self._set_department(settings)
        self._set_document(settings=settings)

    def _set_directories(self, settings: UserSettings) -> None:
        self._gui.directories.scan_directory = settings.scan_dir
        self._gui.directories.dest_directory = settings.dest_dir

    def _set_department(self, settings: UserSettings) -> None:
        department_names = list(map(
            lambda dept: dept.full_name, 
            self._config.database.all_departments()
        ))
        
        self._gui.defaults.department_options = department_names
        self._gui.defaults.department = settings.department.full_name

    def _set_document(
            self, settings: UserSettings = None, department: Department = None
    ) -> None:
        self._set_document_from_user_settings(settings) if settings else (
            self._set_document_from_department(department))

    def _set_document_from_user_settings(self, settings: UserSettings) -> None:
        document_names = list(map(
            lambda d: d.full_name, settings.department.document_types))
        
        self._gui.defaults.document_options = document_names
        self._gui.defaults.document_type = settings.document_type.full_name

    def _set_document_from_department(self, department: Department) -> None:
        document_names = department.document_types.full_names()

        self._gui.defaults.document_options = document_names
        self._gui.defaults.document_type = document_names[0]

    def _settings_from_gui(self) -> UserSettings:
        result = UserSettings()
        result.scan_dir = self._gui.directories.scan_directory
        result.dest_dir = self._gui.directories.dest_directory

        department_name = self._gui.defaults.department
        
        result.department = self._config.database.department(
            full_name=department_name)

        document_name = self._gui.defaults.document_type
        
        result.document_type = self._config.database.document(
            full_name=document_name)

        return result

    @staticmethod
    def _directory_dialog() -> str or None:
        with wx.DirDialog(None) as browser:
            return (
                None if browser.ShowModal() == wx.ID_CANCEL
                else browser.GetPath()
            )
