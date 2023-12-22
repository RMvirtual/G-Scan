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

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        widget_to_flags = {
            self.title: wx.ALIGN_LEFT|wx.ALL,
            self.directories: wx.EXPAND|wx.ALL,
            self.defaults: wx.ALIGN_LEFT|wx.ALL,
            self.save: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,
            self.exit: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM
        }

        for widget, flags in widget_to_flags.items():
            sizer.Add(window=widget, proportion=0, flag=flags, border=15)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)

        self.SetBackgroundColour(colour=wx.WHITE)
