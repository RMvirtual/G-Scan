import wx
from src.main.gui.metrics import screen_size
from src.main.gui.settings.directories import Directories


class Settings(wx.Frame):
    def __init__(self) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(
            parent=None, title="Settings", size=size, pos=position)

        self.directories = Directories(self)

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

        font = wx.Font(wx.FontInfo(pointSize=20).Bold())
        self.save.SetFont(font)
        self.exit.SetFont(font)

        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.directories,
            flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.save, proportion=0,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=15
        )

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=15
        )

        self.SetSizer(sizer)

    def show(self) -> None:
        self.Show()

    def hide(self) -> None:
        self.Hide()

    def close(self) -> None:
        self.Close()
