import wx

from gui.settings.defaults import DefaultsPanel
from gui.settings.directories import DirectoriesPanel


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(window)

        self.title_txt = wx.StaticText(self, label="Settings")
        self.directories = DirectoriesPanel(self)
        self.defaults = DefaultsPanel(self)
        self.save_btn = wx.Button(self, label="Save")
        self.exit_btn = wx.Button(self, label="Exit")

        self.title_txt.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())
        self.save_btn.SetFont(wx.Font(wx.FontInfo(pointSize=12)))
        self.exit_btn.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        
        sizer.Add(
            self.title_txt, proportion=0, flag=wx.ALIGN_LEFT|wx.ALL, border=15)

        sizer.Add(
            self.directories, proportion=0, flag=wx.EXPAND|wx.ALL, border=15)

        sizer.Add(
            self.defaults, proportion=0, flag=wx.ALIGN_LEFT|wx.ALL, border=15)

        sizer.Add(
            self.save_btn, proportion=0, 
            flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=15
        )

        sizer.Add(
            self.exit_btn, proportion=0, flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, 
            border=15
        )

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.WHITE)
