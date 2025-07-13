import wx

from departments import Department


class DepartmentsPanel(wx.Panel):
    def __init__(
        self, parent: wx.Frame, departments: list[Department]
    ) -> None:
        super().__init__(parent)

        self.department_btns: dict[str, wx.Button] = {}

        for dept in departments:
            btn = wx.Button(self, label=dept.short_name, style=wx.BU_EXACTFIT)
            self.department_btns[dept.short_code] = btn

        self.quick_start_btn = wx.Button(self, label="Quick Start")
        self.settings_btn = wx.Button(self, label="Settings")
        self.exit_btn = wx.Button(self, label="Exit")

        all_buttons = [
            *self.department_btns.values(),
            self.quick_start_btn,
            self.settings_btn,
            self.exit_btn,
        ]

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

        for button in all_buttons:
            button.SetFont(font)

        # Sizer layout.
        border = 15
        departments_sizer = wx.WrapSizer(orient=wx.HORIZONTAL)

        for button in *self.department_btns.values(), self.quick_start_btn:
            departments_sizer.Add(button, 0, wx.ALL, border)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(departments_sizer, 1, wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self.settings_btn, 0, wx.ALL | wx.ALIGN_RIGHT, border)
        sizer.Add(self.exit_btn, 0, wx.ALL | wx.ALIGN_RIGHT, border)
        self.SetSizer(sizer)
