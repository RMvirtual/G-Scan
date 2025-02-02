import wx

from gui.settings.defaults import DefaultsPanel
from gui.settings.directories import DirectoriesPanel


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(window)

        self.title = wx.StaticText(self, label="Settings")
        self.directories = DirectoriesPanel(self)
        self.defaults = DefaultsPanel(self)
        self.save = wx.Button(self, label="Save")
        self.exit = wx.Button(self, label="Exit")

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())
        self.save.SetFont(wx.Font(wx.FontInfo(pointSize=12)))
        self.exit.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        # Sizer layout.
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

