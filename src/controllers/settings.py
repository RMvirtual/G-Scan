import wx

from controllers import workflows
from controllers.mediator import ApplicationMediator
from database import UserSettings
from departments import Department
from gui.settings.settings import Settings
from gui.window import Window


class SettingsController:
    def __init__(
            self, app: ApplicationMediator, window: Window,
            dept_options: list[Department], user_settings: UserSettings,
    ) -> None:
        self.app = app
        self.gui = Settings(window)
        self.window = window
        self.user_settings = user_settings
        self.dept_options = dept_options

        # Load settings from configuration.        
        self.gui.directories.output_dir_entry.SetValue(user_settings.output_dir)

        dept_names = list(map(lambda d: d.full_name, dept_options))        
        self.gui.defaults.dept_box.SetItems(dept_names)
        self.gui.defaults.dept_box.SetValue(user_settings.department.full_name)

        self.update_doc_options(user_settings.department)

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
        
        department = [
            d for d in self.dept_options if d.full_name == department_value][0]

        self.update_doc_options(department)

    def update_doc_options(self, department: Department) -> None:
        self.gui.defaults.dept_box.SetValue(department.full_name)
        documents = list(map(lambda d: d.full_name, department.document_types))
        
        self.gui.defaults.doc_box.SetItems(documents)
        self.gui.defaults.doc_box.SetValue(documents[0])

    def on_close(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def exit_to_main_menu(self) -> None:
        self.gui.Close()
        self.app.launch_main_menu()
