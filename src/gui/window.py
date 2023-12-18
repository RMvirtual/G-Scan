import wx

from gui.metrics import recommended_metrics


class Window(wx.Frame):
    def __init__(self):
        size, position = recommended_metrics()
        super().__init__(parent=None, title="", size=size, pos=position)

        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._panel = None
        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self._panel, proportion=1, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.Layout()

    def set_panel(self, panel: wx.Panel) -> None:
        if self._panel:
            self._replace(panel)

        else:
            self._create_panel(panel)

        self.Layout()

    def _create_panel(self, panel: wx.Panel) -> None:
        self._panel = panel
        self._initialise_sizer()

    def _replace(self, panel: wx.Panel) -> None:
        self.GetSizer().Replace(self._panel, panel)
        self._panel = panel