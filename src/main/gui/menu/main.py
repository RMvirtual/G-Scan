import wx
from src.main.gui.app import screen_size
from src.main.gui.menu.departments import Departments
from src.main.gui.menu.logo import Logo


class MainMenu(wx.Frame):
    def __init__(self, title) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)

        self._initialise_panels()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.WHITE)


    def _initialise_panels(self) -> None:
        self._departments = Departments(self)
        self._logo = Logo(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND

        sizer.Add(window=self._logo, proportion=1, flag=flags, border=0)
        sizer.Add(window=self._departments, proportion=2, flag=flags, border=0)

        self.SetSizer(sizer)
