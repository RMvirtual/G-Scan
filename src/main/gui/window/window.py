import wx
from src.main.gui.metrics import screen_size


class Window(wx.Frame):
    def __init__(self):
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title="", size=size, pos=position)
        self._initialise_widgets()
        self.panel = None

    def set_panel(self, panel: wx.Panel) -> None:
        self.panel = panel
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.panel, flag=wx.EXPAND)

        self.SetSizer(sizer)

    def _initialise_widgets(self) -> None:
        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_status_bar(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("HELLO WORLD")

    @property
    def status_bar(self) -> str:
        return self.GetStatusText()

    @status_bar.setter
    def status_bar(self, new_status: str) -> None:
        self.SetStatusText(new_status)
