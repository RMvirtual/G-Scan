import wx
from src.main.gui.metrics import screen_size


class Settings(wx.Frame):
    def __init__(self) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(
            parent=None, title="Settings", size=size, pos=position)

        self._initialise_widgets()
        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_widgets(self) -> None:
        self.scan_dir_label = wx.StaticText(
            parent=self, label="Scan Directory")

        self.scan_dir_box = wx.TextCtrl(parent=self, value="NULL")
        self.scan_dir_browse = wx.Button(parent=self, label="...")

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer()
        sizer.Add(window=self.scan_dir_label, pos=(0,0))
        sizer.Add(window=self.scan_dir_box, pos=(1,0))
        sizer.Add(window=self.scan_dir_browse, pos=(2,0))

    def show(self) -> None:
        self.Show()

    def hide(self) -> None:
        self.Hide()

    def close(self) -> None:
        self.Close()
