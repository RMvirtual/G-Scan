import wx
from src.main.gui.settings.directories import Directories
from src.main.gui.settings.defaults import Defaults


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(parent=window)

        self._initialise_widgets()
        self._initialise_fonts()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_widgets(self) -> None:
        self.title = wx.StaticText(parent=self, label="Settings")
        self.directories = Directories(self)
        self.defaults = Defaults(self)

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

    def _initialise_fonts(self) -> None:
        title_font = wx.Font(wx.FontInfo(pointSize=30).Bold())
        self.title.SetFont(title_font)

        smaller_font = wx.Font(wx.FontInfo(pointSize=12))
        self.save.SetFont(smaller_font)
        self.exit.SetFont(smaller_font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.title, proportion=0,
            flag=wx.ALIGN_LEFT|wx.ALL, border=15
        )

        sizer.Add(
            window=self.directories, proportion=0,
            flag=wx.EXPAND|wx.ALL, border=15
        )

        sizer.Add(
            window=self.defaults, proportion=0,
            flag=wx.ALIGN_LEFT|wx.ALL, border=15
        )

        nav_aligns = wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM

        sizer.Add(window=self.save, proportion=0, flag=nav_aligns, border=15)
        sizer.Add(window=self.exit, proportion=0, flag=nav_aligns, border=15)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)

    def show(self) -> None:
        self.Show()

    def hide(self) -> None:
        self.Hide()

    def close(self) -> None:
        self.Close()
