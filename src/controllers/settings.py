import wx

from configuration import Configuration
from controllers import workflows
from controllers.selector import AppSelector
from database import UserSettings
from gui.settings.settings import Settings
from gui.window import Window


class SettingsController:
    def __init__(
            self, root: AppSelector, config: Configuration, window: Window
    ) -> None:
        self.root = root
        self.config = config
        self.gui = Settings(window)
        self.window = window

        # Load settings from configuration.        
        settings = config.settings
        self.set_dest_directory_entry(settings.dest_dir)
        
        self.gui.defaults.department_options = list(map(
            lambda d: d.full_name, self.config.database.all_departments()))
        
        self.gui.defaults.department = settings.department.full_name
        
        self.gui.defaults.document_options = list(map(
            lambda d: d.full_name, settings.department.document_types))

        self.gui.defaults.document_type = settings.document_type.full_name

        self.window.Layout()
        window.set_panel(self.gui)

        # Bind callbacks.
        self.gui.save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)
        
        self.gui.directories.output_dir_btn.Bind(
            wx.EVT_BUTTON, self.on_output_directory_browse)

        self.gui.defaults.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_option_change)

        self.gui.Bind(wx.EVT_CLOSE, self.on_close)

    def on_save(self, event: wx.Event) -> None:
        database = self.config.database
        defaults = self.gui.defaults

        new_settings = UserSettings(
            self.config.settings.username,
            self.gui.directories.dest_directory,
            database.department(full_name=defaults.department),
            database.document(full_name=defaults.document_type)
        )

        database.save_user_settings(new_settings)
        self.config.settings = new_settings
        self.exit_to_main_menu()

    def on_exit(self, event: wx.Event) -> None:
        self.exit_to_main_menu()

    def on_output_directory_browse(self, event: wx.Event) -> None:
        directory = workflows.request_directory()

        if directory is not None:
            self.set_dest_directory_entry(directory)

    def on_department_option_change(self, event: wx.Event) -> None:
        defaults_frame = self.gui.defaults

        department = self.config.database.department(
            full_name=defaults_frame.department)

        documents = list(map(lambda d: d.full_name, department.document_types))
        defaults_frame.document_options = documents
        defaults_frame.document_type = documents[0]

    def on_close(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def exit_to_main_menu(self) -> None:
        self.gui.Close()
        self.root.launch_main_menu()

    def dest_directory_entry(self) -> str:
        return self.gui.directories.output_dir_entry.GetValue()

    def set_dest_directory_entry(self, directory: str) -> None:
        self.gui.directories.output_dir_entry.SetValue(directory)
