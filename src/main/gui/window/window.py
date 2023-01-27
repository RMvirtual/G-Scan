import wx
from src.main.gui.metrics import screen_size


class Window(wx.Frame):
    def __init__(self):
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title="", size=size, pos=position)
        self.SetDoubleBuffered(True)

        self._panel = None
        self.SetBackgroundColour(colour=wx.WHITE)

    @property
    def panel(self) -> wx.Panel:
        return self.panel

    @panel.setter
    def panel(self, panel: wx.Panel) -> None:
        self._panel = panel
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self._panel, proportion=1, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.Layout()

    def _initialise_status_bar(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("HELLO WORLD")

    @property
    def status_bar(self) -> str:
        return self.GetStatusText()

    @status_bar.setter
    def status_bar(self, new_status: str) -> None:
        self.SetStatusText(new_status)
