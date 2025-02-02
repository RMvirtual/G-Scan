import wx

from gui.main_menu.departments.settings_toolbar import SettingsToolbar


class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)
        self.options = DepartmentOptions(self)
        self.toolbar = SettingsToolbar(self)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(window=self.toolbar, proportion=0, flag=wx.ALIGN_RIGHT)
        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        button_labels = ["Ops", "PODs", "Quick Start"]
        buttons = [wx.Button(self, label=label) for label in button_labels]

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in buttons:
            button.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

            sizer.Add(
                button, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP,
                border=15
            )

        self.SetSizer(sizer)
        self.ops, self.pods, self.quick_start = buttons
