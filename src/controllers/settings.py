import wx

from configuration import Configuration
from database import UserSettings
from departments import Department
from gui.settings_dialog import SettingsDialog


class SettingsDialogController:
    def __init__(
        self,
        parent: wx.Frame,
        config: Configuration,
    ) -> None:
        self.gui = SettingsDialog(parent)
        self.config = config
        self.user_settings = config.settings

        # Load settings from configuration.
        self.gui.output_directory_entry.SetValue(self.user_settings.output_dir)
        dept_box = self.gui.department_box
        dept_box.Set(list(map(lambda d: d.full_name, self.config.departments)))
        dept_box.SetValue(self.user_settings.department.full_name)

        self.update_options(self.user_settings.department)

        # Bind callbacks.
        self.gui.save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)

        self.gui.output_directory_btn.Bind(
            wx.EVT_BUTTON, self.on_output_directory_browse
        )

        self.gui.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_change
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

    def update_options(self, department: Department) -> None:
        names = [document.full_name for document in department.document_types]

        panel = self.gui
        panel.department_box.SetValue(department.full_name)
        panel.document_box.SetItems(names)
        panel.document_box.SetValue(names[0])

    def poll(self) -> None:
        self.gui.Show()
        self.gui.Fit()
        self.gui.SetFocus()

        with self.gui:
            print(self.gui.ShowModal())

        return None

    def on_save(self, event: wx.Event) -> None:
        dept_value = self.gui.department_box.GetValue()

        dept = list(
            filter(
                lambda d: d.full_name == dept_value, self.config.departments
            )
        )[0]

        document_value = self.gui.document_box.GetValue()

        document = list(
            filter(
                lambda d: d.full_name == document_value, dept.document_types
            )
        )[0]

        output_directory = self.gui.output_directory_entry.GetValue()

        new_settings = UserSettings(
            self.user_settings.username, output_directory, dept, document
        )

        self.user_settings.update(new_settings)

    def on_output_directory_browse(self, event: wx.Event) -> None:
        dialog = wx.DirDialog(parent=None)

        with dialog:
            directory = (
                dialog.GetPath() if dialog.ShowModal() == wx.ID_OK else None
            )

        if directory is not None:
            self.gui.output_directory_entry.SetValue(directory)

    def on_department_change(self, event: wx.Event) -> None:
        current_name = self.gui.department_box.GetValue()

        matching_departments = filter(
            lambda d: d.full_name == current_name, self.config.departments
        )

        department = list(matching_departments)[0]
        self.update_options(department)

    def on_exit(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def on_f4_escape_key(self, event: wx.Event) -> None:
        self.on_exit(event)
