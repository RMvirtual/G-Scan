import wx
from src.main.gui.app import screen_size
from src.main.gui.menu.initial_options import InitialOptions
from src.main.gui.menu.logo import Logo


class MainMenu(wx.Frame):
    def __init__(self, title) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)

        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
        self._initial_options = InitialOptions(self)
        self._logo = Logo(self)

        self._sizer = wx.BoxSizer(orient=wx.VERTICAL)

        self._sizer.AddStretchSpacer()

        self._sizer.Add(
            window=self._logo, proportion=1, flag=wx.EXPAND, border=0)

        self._sizer.Add(
            window=self._initial_options, proportion=1, flag=wx.EXPAND,
            border=0
        )

        self._sizer.AddStretchSpacer()

        self.SetSizer(self._sizer)
