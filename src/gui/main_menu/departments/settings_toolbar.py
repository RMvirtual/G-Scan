import wx


class SettingsToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)

        self.settings = wx.Button(parent=self, label="Settings")
        self.exit = wx.Button(parent=self, label="Exit")

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        for widget in [self.settings, self.exit]:
            font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

            widget.SetFont(font)

            sizer.Add(
                widget, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)
