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

        self.dest_dir_label = wx.StaticText(
            parent=self, label="Destination Directory")

        self.dest_dir_box = wx.TextCtrl(parent=self, value="NULL")
        self.dest_dir_browse = wx.Button(parent=self, label="...")

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        items = [
            self.scan_dir_label, self.scan_dir_box, self.scan_dir_browse,
            self.dest_dir_label, self.dest_dir_box, self.dest_dir_browse,
            self.save, self.exit
        ]

        for item in items:
            item.SetFont(font)


    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer()
        sizer.Add(window=self.scan_dir_label, pos=(0,0), flag=wx.EXPAND)
        sizer.Add(window=self.scan_dir_box, pos=(0,1), flag=wx.EXPAND)
        sizer.Add(window=self.scan_dir_browse, pos=(0,2), flag=wx.EXPAND)

        sizer.Add(window=self.dest_dir_label, pos=(1,0), flag=wx.EXPAND)
        sizer.Add(window=self.dest_dir_box, pos=(1,1), flag=wx.EXPAND)
        sizer.Add(window=self.dest_dir_browse, pos=(1,2), flag=wx.EXPAND)

        sizer.Add(window=self.save, pos=(2,0), flag=wx.EXPAND)
        sizer.Add(window=self.exit, pos=(2,1), flag=wx.EXPAND)

        self.SetSizer(sizer)

    def show(self) -> None:
        self.Show()

    def hide(self) -> None:
        self.Hide()

    def close(self) -> None:
        self.Close()
