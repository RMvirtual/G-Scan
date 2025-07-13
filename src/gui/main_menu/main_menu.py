import wx

from departments import Department
from gui.main_menu.department import DepartmentsPanel
from gui.main_menu.logo import LogoPanel


class MainMenu(wx.Panel):
    def __init__(
        self, parent: wx.Frame, departments: list[Department]
    ) -> None:
        super().__init__(parent)

        self.logo = LogoPanel(self)
        self.panel = DepartmentsPanel(self, departments)

        # Sizer layout.
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizer.Add(self.logo, proportion=2, flag=wx.EXPAND)
        self.sizer.Add(self.panel, proportion=3, flag=wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetBackgroundColour(colour=wx.WHITE)

    def switch_to(self, new_panel: wx.Panel) -> None:
        self.sizer.Clear()
        self.panel.Destroy()
        self.panel = new_panel

        # Sizer layout.
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizer.Add(self.logo, proportion=2, flag=wx.EXPAND)
        self.sizer.Add(self.panel, proportion=3, flag=wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Layout()
