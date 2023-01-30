import wx


class FilesPanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super(FilesPanel, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self._title = wx.StaticText(parent=self, label="Jobs")
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())
        self._title.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self._title, proportion=0, flag=wx.EXPAND, border=5)
        self.SetSizer(sizer)
