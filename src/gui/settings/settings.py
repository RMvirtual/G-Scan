import wx

from gui import fonts
from gui.settings.directories import Directories
from gui.settings.defaults import Defaults


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(parent=window)

        self.title = wx.StaticText(parent=self, label="Settings")
        self.title.SetFont(fonts.font(point_size=30, bold=True))

        self.directories = Directories(self)
        self.defaults = Defaults(self)

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

        font = fonts.font(point_size=12)
        self.save.SetFont(font)
        self.exit.SetFont(font)

        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.WHITE)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        widget_to_flags = {
            self.title: wx.ALIGN_LEFT|wx.ALL,
            self.directories: wx.EXPAND|wx.ALL,
            self.defaults: wx.ALIGN_LEFT|wx.ALL,
            self.save: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,
            self.exit: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM
        }

        sizer.Add(
            window=self.title, proportion=0, flag=wx.ALIGN_LEFT|wx.ALL, 
            border=15
        )

        sizer.Add(
            window=self.directories, proportion=0, flag=wx.EXPAND|wx.ALL, 
            border=15
        )

        sizer.Add(
            window=self.defaults, proportion=0, flag=wx.ALIGN_LEFT|wx.ALL,
            border=15
        )

        for button in (self.save, self.exit):
            sizer.Add(
                window=button, proportion=0, 
                flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=15
            )

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)
