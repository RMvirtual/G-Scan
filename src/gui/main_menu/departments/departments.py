import wx
from departments import Department


class DepartmentsPanel(wx.Panel):
    def __init__(
            self, parent: wx.Frame, departments: list[Department]) -> None:
        super().__init__(parent)

        self.dept_btns: dict[str, wx.Button] = {}

        for department in departments:
            dept_btn = wx.Button(self, label=department.short_name)
            self.dept_btns[department.short_code] = dept_btn

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
        depts_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        depts_flag = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP

        for button in *self.dept_btns.values(), self.quick_start_btn:
            depts_sizer.Add(button, proportion=0, flag=depts_flag, border=15)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(depts_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        bottom_flag = wx.ALL|wx.ALIGN_RIGHT
        sizer.Add(self.settings_btn, proportion=0, flag=bottom_flag, border=15)
        sizer.Add(self.exit_btn, proportion=0, flag=bottom_flag, border=15)
        self.SetSizer(sizer)
