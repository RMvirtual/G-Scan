import wx
from src.main.gui.main_menu.departments import Departments, Operations
from src.main.gui.main_menu.logo import Logo


class MainMenu(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent=parent)

        self._initialise_panels()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_panels(self) -> None:
        self.logo = Logo(self)
        self.departments = Departments(self)
        self.operations = Operations(self)

        self.operations.Hide()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND

        sizer.Add(window=self.logo, proportion=2, flag=flags, border=0)
        sizer.Add(window=self.departments, proportion=3, flag=flags, border=0)
        sizer.Add(window=self.operations, proportion=3, flag=flags, border=0)

        self.SetSizer(sizer)

    def view_ops(self, event = None) -> None:
        self.departments.Hide()
        self.operations.Show()

        self.Layout()

    def view_departments(self, event = None) -> None:
        self.operations.Hide()
        self.departments.Show()

        self.Layout()

    def close(self) -> None:
        self.Close()
