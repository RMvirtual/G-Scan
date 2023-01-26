import wx


class SettingsToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(SettingsToolbar, self).__init__(parent=parent)

        self._initialise_buttons()
        self._initialise_sizer()

    def _initialise_buttons(self) -> None:
        self.settings = wx.Button(parent=self, label="Settings")
        self.exit = wx.Button(parent=self, label="Exit")

        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        self.settings.SetFont(font)
        self.exit.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.settings, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=15
        )

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=15
        )

        self.SetSizer(sizer)