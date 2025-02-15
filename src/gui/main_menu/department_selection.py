import wx

from departments import Department


class DepartmentSelectionPanel(wx.Panel):
    def __init__(
            self, parent: wx.Frame, departments: list[Department]) -> None:
        super().__init__(parent)

        self.dept_btns: dict[str, wx.Button] = {}

        for department in departments:
            self.dept_btns[department.short_code] = wx.Button(
                self, label=department.short_name, style=wx.BU_EXACTFIT)

        self.quick_start_btn = wx.Button(self, label="Quick Start")
        self.settings_btn = wx.Button(self, label="Settings")
        self.exit_btn = wx.Button(self, label="Exit")

        all_buttons =  [
            *self.dept_btns.values(), self.quick_start_btn, 
            self.settings_btn, self.exit_btn
        ]

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()
        
        for button in all_buttons:
            button.SetFont(font)

        # Sizer layout.
        depts_sizer = wx.WrapSizer(orient=wx.HORIZONTAL)

        for button in *self.dept_btns.values(), self.quick_start_btn:
            depts_sizer.Add(button, proportion=0, flag=wx.ALL, border=15)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(depts_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        bottom_flag = wx.ALL|wx.ALIGN_RIGHT
        sizer.Add(self.settings_btn, proportion=0, flag=bottom_flag, border=15)
        sizer.Add(self.exit_btn, proportion=0, flag=bottom_flag, border=15)
        self.SetSizer(sizer)
