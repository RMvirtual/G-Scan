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

        self._files = wx.TreeCtrl(parent=self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self._title, proportion=0,
            flag=wx.ALIGN_CENTRE_HORIZONTAL, border=5
        )

        sizer.Add(
            window=self._files, proportion=0,
            flag=wx.EXPAND|wx.ALL, border=5
        )

        self.SetSizer(sizer)
