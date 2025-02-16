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
        self.set_dest_directory_entry(user_settings.dest_dir)
        
        self.set_department_options(
            list(map(lambda d: d.full_name, dept_options)))
        
        self.set_department(user_settings.department.full_name)
        
        self.set_document_options(list(map(
            lambda d: d.full_name, user_settings.department.document_types)))

        self.set_document_type(user_settings.document_type.full_name)

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
        department_selection = list(filter(
            lambda d: d.full_name == self.department(), self.dept_options))
        
        if not department_selection:
            return
        
        default_department = department_selection[0]

        document_selection = list(filter(
            lambda d: d.full_name == self.document_type(), 
            default_department.document_types
        )
        )
        if not document_selection:
            return

        default_document = document_selection[0]

        new_settings = UserSettings(
            self.user_settings.username, self.dest_directory_entry(),
            default_department, default_document
        )

        self.app.update_user_settings(new_settings)
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
            full_name=self.department())

        documents = list(map(lambda d: d.full_name, department.document_types))
        self.set_document_options(documents)
        self.set_document_type(documents[0])

    def on_close(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def exit_to_main_menu(self) -> None:
        self.gui.Close()
        self.app.launch_main_menu()

    def dest_directory_entry(self) -> str:
        return self.gui.directories.output_dir_entry.GetValue()

    def set_dest_directory_entry(self, directory: str) -> None:
        self.gui.directories.output_dir_entry.SetValue(directory)

    def department(self) -> str:
        return self.gui.defaults.dept_box.GetValue()

    def set_department(self, new_department: str) -> None:
        self.gui.defaults.dept_box.SetValue(new_department)

    def department_options(self) -> str:
        return self.gui.defaults.dept_box.GetItems()

    def set_department_options(self, options: list[str]) -> None:
        self.gui.defaults.dept_box.SetItems(options)

    def document_type(self) -> str:
        return self.gui.defaults.doc_box.GetValue()

    def set_document_type(self, new_document_type: str) -> None:
        self.gui.defaults.doc_box.SetValue(new_document_type)

    def document_options(self) -> list[str]:
        return self.gui.defaults.doc_box.GetItems()

    def set_document_options(self, new_options: list[str]) -> None:
        self.gui.defaults.doc_box.SetItems(new_options)
