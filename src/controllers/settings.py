import wx

from configuration import Configuration
from controllers import workflows
from gui.settings.settings import Settings
from gui.window import Window
from root_interface import RootInterface
from user import UserSettings


class SettingsController:
    def __init__(
            self, root_application: RootInterface, 
            config: Configuration,
            window: Window
    ) -> None:
        self._root = root_application
        self._config = config
        self._gui = Settings(window)
        self._window = window

        # Load settings from configuration.        
        settings = config.settings

        department_names = list(map(
            lambda d: d.full_name, self._config.database.all_departments()))

        document_names = list(map(
            lambda d: d.full_name, settings.department.document_types))

        dirs_frame = self._gui.directories
        dirs_frame.scan_directory = settings.scan_dir
        dirs_frame.dest_directory = settings.dest_dir

        defaults_frame = self._gui.defaults
        defaults_frame.department_options = department_names
        defaults_frame.department = settings.department.full_name
        defaults_frame.document_options = document_names

        defaults_frame.document_type = settings.document_type.full_name

        self._window.Layout()
        window.set_panel(self._gui)

        # Bind callbacks.
        self._gui.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._gui.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        dirs_frame.scan_box.button.Bind(wx.EVT_BUTTON, self.on_scan_dir_browse)
        dirs_frame.dest_box.button.Bind(wx.EVT_BUTTON, self.on_dest_dir_browse)

        defaults_frame.department_option.box.Bind(
            wx.EVT_COMBOBOX, self.on_department_option_change)

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

    def on_save(self, event: wx.Event) -> None:
        database = self._config.database
        defaults = self._gui.defaults
        department = database.department(full_name=defaults.department)
        document_type = database.document(full_name=defaults.document_type)

        new_settings = UserSettings(
            username=self._config.settings.username,
            scan_dir=self._gui.directories.scan_directory,
            dest_dir=self._gui.directories.dest_directory,
            department=department,
            document_type=document_type
        )

        database.save_user_settings(new_settings)
        self._config.settings = new_settings
        self._exit_to_main_menu()

    def on_exit(self, event: wx.Event) -> None:
        self._exit_to_main_menu()

    def on_scan_dir_browse(self, event: wx.Event) -> None:
        directory = workflows.request_directory()

        if directory is not None:
            self._gui.directories.scan_directory = directory

    def on_dest_dir_browse(self, event: wx.Event) -> None:
        directory = workflows.request_directory()

        if directory is not None:
            self._gui.directories.dest_directory = directory

    def on_department_option_change(self, event: wx.Event) -> None:
        defaults_frame = self._gui.defaults

        department = self._config.database.department(
            full_name=defaults_frame.department)

        documents = list(map(lambda d: d.full_name, department.document_types))
        defaults_frame.document_options = documents
        defaults_frame.document_type = documents[0]

    def on_close(self, event: wx.Event) -> None:
        self._gui.Destroy()

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()
