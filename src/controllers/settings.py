import wx

from configuration import Configuration
from database import UserSettings
from departments import Department
from documents import DocumentType
from gui.settings_dialog import SettingsDialog


class SettingsDialogController:
    def __init__(self, parent: wx.Frame, config: Configuration) -> None:
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
        self.gui.department_box.SetValue(department.full_name)

        document_types = [
            document.full_name for document in department.document_types
        ]

        self.gui.document_box.Set(document_types)
        self.gui.document_box.SetValue(document_types[0])

    def poll(self) -> None:
        self.gui.Show()
        self.gui.Fit()
        self.gui.SetFocus()

        with self.gui:
            print(self.gui.ShowModal())

        return None

    def on_save(self, event: wx.Event) -> None:
        new_settings = UserSettings(
            self.user_settings.username,
            self.gui.output_directory_entry.GetValue(),
            self.department_from_box(),
            self.document_type_from_box(),
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
        new_department = self.department_from_box()

        if new_department is not None:
            self.update_options(new_department)

    def on_exit(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def on_f4_escape_key(self, event: wx.Event) -> None:
        self.on_exit(event)

    def department_from_box(self) -> Department | None:
        current_name = self.gui.department_box.GetValue()

        matching_departments = list(
            filter(
                lambda d: d.full_name == current_name, self.config.departments
            )
        )

        return matching_departments[0] if matching_departments else None

    def document_type_from_box(self) -> DocumentType | None:
        current_name = self.gui.document_box.GetValue()

        matching_types = list(
            filter(
                lambda d: d.full_name == current_name,
                self.config.department.document_types,
            )
        )

        return matching_types[0] if matching_types else None
