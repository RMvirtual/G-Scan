import wx
from src.main.gui import fonts


class NewToolBar(wx.ToolBar):
    def __init__(self, parent: wx.Window):
        super(NewToolBar, self).__init__(
            parent=parent, style=wx.TB_TEXT|wx.TB_FLAT)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.open = wx.Button(parent=self, label="Open")

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer.Add(window=self.open, proportion=0, border=5)

        self.SetSizer(sizer)
