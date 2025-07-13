import wx

from controllers import workflows
from controllers.mediator import ApplicationMediator
from database import UserSettings
from departments import Department
from gui.settings import Settings
from gui.window import Window


class SettingsController:
    def __init__(
        self,
        app: ApplicationMediator,
        window: Window,
        dept_options: list[Department],
        user_settings: UserSettings,
    ) -> None:
        self.app = app
        self.gui = Settings(window)
        self.user_settings = user_settings
        self.dept_options = dept_options

        # Load settings from configuration.
        self.gui.output_directory_entry.SetValue(user_settings.output_dir)

        dept_names = list(map(lambda d: d.full_name, self.dept_options))
        self.gui.department_box.SetItems(dept_names)
        self.gui.department_box.SetValue(user_settings.department.full_name)

        self.update_options(user_settings.department)

        # Bind callbacks.
        self.gui.save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)

        self.gui.output_directory_btn.Bind(
            wx.EVT_BUTTON, self.on_output_directory_browse
        )

        self.gui.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_option_change
        )

        # Shortcut keys.
        f4_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4_escape_key, id=f4_shortcut_id)

        esc_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4_escape_key, id=esc_shortcut_id)

        accelators = [
            (wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id),
            (wx.ACCEL_NORMAL, wx.WXK_ESCAPE, esc_shortcut_id),
        ]

        self.gui.SetAcceleratorTable(wx.AcceleratorTable(accelators))
        self.gui.SetFocus()

    def update_options(self, department: Department) -> None:
        names = [document.full_name for document in department.document_types]

        panel = self.gui
        panel.department_box.SetValue(department.full_name)
        panel.document_box.SetItems(names)
        panel.document_box.SetValue(names[0])

    def exit_to_main_menu(self) -> None:
        self.gui.Destroy()
        self.app.launch_main_menu()

    def on_save(self, event: wx.Event) -> None:
        dept_value: str = self.gui.department_box.GetValue()

        dept = list(
            filter(lambda d: d.full_name == dept_value, self.dept_options)
        )[0]

        document_value = self.gui.document_box.GetValue()

        document = list(
            filter(
                lambda d: d.full_name == document_value, dept.document_types
            )
        )[0]

        output_directory = self.gui.output_directory_entry.GetValue()

        settings = UserSettings(
            self.user_settings.username, output_directory, dept, document
        )

        self.app.update_user_settings(settings)
        self.exit_to_main_menu()

    def on_exit(self, event: wx.Event) -> None:
        self.exit_to_main_menu()

    def on_output_directory_browse(self, event: wx.Event) -> None:
        directory = workflows.request_directory()

        if directory is not None:
            self.gui.output_directory_entry.SetValue(directory)

    def on_department_option_change(self, event: wx.Event) -> None:
        department_value = self.gui.department_box.GetValue()

        department = [
            d for d in self.dept_options if d.full_name == department_value
        ][0]

        self.update_options(department)

    def on_f4_escape_key(self, event: wx.Event) -> None:
        self.exit_to_main_menu()
