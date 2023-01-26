import wx
from src.main.gui.app import screen_size
from src.main.gui.menu.departments import Departments
from src.main.gui.menu.logo import Logo
from src.main.gui.menu.operations import OperationsOptions

class MainMenu(wx.Frame):
    def __init__(self, title) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)

        self._initialise_panels()
        self._initialise_sizer()
        self._initialise_callbacks()
        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_panels(self) -> None:
        self._logo = Logo(self)
        self._departments = Departments(self)
        self._operations = OperationsOptions(self)

        self._operations.Hide()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND

        sizer.Add(window=self._logo, proportion=1, flag=flags, border=0)
        sizer.Add(window=self._departments, proportion=2, flag=flags, border=0)
        sizer.Add(window=self._operations, proportion=2, flag=flags, border=0)

        self.SetSizer(sizer)

    def _initialise_callbacks(self) -> None:
        self._departments.ops.Bind(wx.EVT_BUTTON, self._view_ops)

    def _view_ops(self, event=None) -> None:
        self._departments.Hide()
        self._operations.Show()

        self.Layout()