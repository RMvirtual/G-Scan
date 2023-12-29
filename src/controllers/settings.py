import wx

from configuration import AppConfiguration, RootInterface
from user import UserSettings
from views import Settings


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
        self._load_settings_from_config()

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

    def _load_settings_from_config(self) -> None:
        departments = list(map(
            lambda dept: dept.full_name, 
            self._config.database.all_departments()
        ))

        documents = list(map(
            lambda d: d.full_name,
            self._config.settings.department.document_types
        ))

        self._gui.directories.scan_directory = self._config.settings.scan_dir
        self._gui.directories.dest_directory = self._config.settings.dest_dir
        self._gui.defaults.department_options = departments
        self._gui.defaults.department = self._config.settings.department.full_name

        self._gui.defaults.document_options = documents

        self._gui.defaults.document_type = (
            self._config.settings.document_type.full_name)

        self._root.window.Layout()

    def _refresh_document_options(self) -> None:
        department = self._config.database.department(
            full_name=self._gui.defaults.department)

        documents = list(map(lambda d: d.full_name, department.document_types))

        self._gui.defaults.document_options = documents
        self._gui.defaults.document_type = documents[0]

    def _settings_from_gui(self) -> UserSettings:
        return UserSettings(
            username=self._config.settings.username,
            scan_dir=self._gui.directories.scan_directory,
            dest_dir=self._gui.directories.dest_directory,
            department=self._config.database.department(
                full_name=self._gui.defaults.department
            ),
            document_type=self._config.database.document(
                full_name=self._gui.defaults.document_type
            )
        )

    @staticmethod
    def _directory_dialog() -> str or None:
        with wx.DirDialog(None) as browser:
            return (
                None if browser.ShowModal() == wx.ID_CANCEL
                else browser.GetPath()
            )
