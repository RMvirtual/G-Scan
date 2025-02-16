import wx

from configuration import Configuration
from controllers import workflows
from controllers.mediator import ApplicationMediator
from database import UserSettings
from departments import Department, DocumentType
from gui.settings.settings import Settings
from gui.window import Window


class SettingsController:
    def __init__(
            self, app: ApplicationMediator, config: Configuration, window: Window,
            dept_options: list[Department], user_settings: UserSettings,
    ) -> None:
        self.app = app
        self.config = config
        self.gui = Settings(window)
        self.window = window
        self.user_settings = user_settings
        self.dept_options = dept_options

        # Load settings from configuration.        
        self.gui.directories.output_dir_entry.SetValue(user_settings.dest_dir)
        
        self.gui.defaults.dept_box.SetItems(
            list(map(lambda d: d.full_name, dept_options)))
        
        self.gui.defaults.dept_box.SetValue(user_settings.department.full_name)
        
        self.gui.defaults.doc_box.SetItems(list(map(
            lambda d: d.full_name, user_settings.department.document_types)))

        self.gui.defaults.doc_box.SetValue(
            user_settings.document_type.full_name)

        self.window.Layout()
        window.set_panel(self.gui)

        # Bind callbacks.
        self.gui.save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)
        
        self.gui.directories.output_dir_btn.Bind(
            wx.EVT_BUTTON, self.on_output_directory_browse)

        self.gui.defaults.dept_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_option_change)

        self.gui.Bind(wx.EVT_CLOSE, self.on_close)

    def on_save(self, event: wx.Event) -> None:
        department_value = self.gui.defaults.dept_box.GetValue()

        department_selection: list[Department] = list(filter(
            lambda d: d.full_name == department_value, self.dept_options))
        
        if not department_selection:
            return
        
        default_department = department_selection[0]
        document_value = self.gui.defaults.doc_box.GetValue()

        document_selection = list(filter(
            lambda d: d.full_name == document_value, 
            default_department.document_types
        ))
        
        if not document_selection:
            return

        default_document = document_selection[0]
        output_directory = self.gui.directories.output_dir_entry.GetValue()

        new_settings = UserSettings(
            self.user_settings.username, output_directory, default_department, 
            default_document
        )

        self.app.update_user_settings(new_settings)
        self.exit_to_main_menu()

    def on_exit(self, event: wx.Event) -> None:
        self.exit_to_main_menu()

    def on_output_directory_browse(self, event: wx.Event) -> None:
        directory = workflows.request_directory()

        if directory is not None:
            self.gui.directories.output_dir_entry.SetValue(directory)

    def on_department_option_change(self, event: wx.Event) -> None:
        department_value = self.gui.defaults.dept_box.GetValue()

        department = self.config.database.department(
            full_name=department_value)

        documents = list(map(lambda d: d.full_name, department.document_types))
        
        self.gui.defaults.doc_box.SetItems(documents)
        self.gui.defaults.doc_box.SetValue(documents[0])

    def on_close(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def exit_to_main_menu(self) -> None:
        self.gui.Close()
        self.app.launch_main_menu()
