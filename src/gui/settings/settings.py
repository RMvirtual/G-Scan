import wx

from gui.settings.defaults import DefaultsPanel
from gui.settings.directories import DirectoriesPanel


class Settings(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Settings")
        self.directories = DirectoriesPanel(self)
        self.defaults = DefaultsPanel(self)
        self.save_btn = wx.Button(self, label="Save")
        self.exit_btn = wx.Button(self, label="Exit")

        # Fonts.
        title_font = wx.Font(wx.FontInfo(pointSize=30)).Bold()
        self.title_lbl.SetFont(title_font)

        size_12_font = wx.Font(wx.FontInfo(pointSize=12))
        self.save_btn.SetFont(size_12_font)
        self.exit_btn.SetFont(size_12_font)

        # Sizer layout.
        border = 15
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        align_left = wx.ALIGN_LEFT | wx.ALL
        sizer.Add(self.title_lbl, 0, align_left, border)
        sizer.Add(self.directories, 0, wx.EXPAND | wx.ALL, border)
        sizer.Add(self.defaults, 0, align_left, border)

        align_bottom_right = wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM
        sizer.Add(self.save_btn, 0, align_bottom_right, border)
        sizer.Add(self.exit_btn, 0, align_bottom_right, border)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.WHITE)
