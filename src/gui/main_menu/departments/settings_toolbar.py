import wx


class SettingsToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()
        
        self.settings_btn = wx.Button(self, label="Settings")
        self.settings_btn.SetFont(font)

        self.exit_btn = wx.Button(self, label="Exit")
        self.exit_btn.SetFont(font)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        alignment_flags = wx.ALL|wx.ALIGN_RIGHT

        sizer.Add(
            self.settings_btn, proportion=0, flag=alignment_flags, border=15)

        sizer.Add(self.exit_btn, proportion=0, flag=alignment_flags, border=15)
        self.SetSizer(sizer)
