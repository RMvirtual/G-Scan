import wx
from src.main.gui.settings.directories import Directories


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(parent=window)

        self.title = wx.StaticText(parent=self, label="Settings")
        self.directories = Directories(self)

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

        title_font = wx.Font(wx.FontInfo(pointSize=30).Bold())
        self.title.SetFont(title_font)

        smaller_font = wx.Font(wx.FontInfo(pointSize=20).Bold())
        self.save.SetFont(smaller_font)
        self.exit.SetFont(smaller_font)

        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.title,
            flag=wx.ALIGN_LEFT|wx.ALL, border=15
        )

        sizer.Add(
            window=self.directories, proportion=1,
            flag=wx.ALIGN_LEFT|wx.ALL, border=15
        )

        sizer.Add(
            window=self.save, proportion=0,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=15
        )

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=15
        )

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)

    def show(self) -> None:
        self.Show()

    def hide(self) -> None:
        self.Hide()

    def close(self) -> None:
        self.Close()
