import wx
from src.main.gui.metrics import screen_size
from src.main.gui.menu.departments import Departments
from src.main.gui.menu.logo import Logo
from src.main.gui.menu.operations import Operations

class MainMenu(wx.Frame):
    def __init__(self, title) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)

        self.SetDoubleBuffered(True)

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

        sizer.Add(window=self.logo, proportion=1, flag=flags, border=0)
        sizer.Add(window=self.departments, proportion=2, flag=flags, border=0)
        sizer.Add(window=self.operations, proportion=2, flag=flags, border=0)

        self.SetSizer(sizer)

    def view_ops(self, event = None) -> None:
        self.departments.Hide()
        self.operations.Show()

        self.Layout()

    def view_departments(self, event = None) -> None:
        self.operations.Hide()
        self.departments.Show()

        self.Layout()
