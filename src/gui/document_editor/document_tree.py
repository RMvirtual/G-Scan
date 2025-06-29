import wx


class DocumentTreePanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent=parent)
        self.title_lbl = wx.StaticText(parent=self, label="Jobs")
        self.title_lbl.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())
        self.upload_btn = wx.Button(parent=self, label="Upload to FCL")

        tree_style = (
            wx.TR_HIDE_ROOT
            | wx.TR_TWIST_BUTTONS
            | wx.TR_HAS_BUTTONS
            | wx.TR_NO_LINES
            | wx.TR_MULTIPLE
        )

        self.tree_ctrl = wx.TreeCtrl(self, style=tree_style)

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.title_lbl,
            proportion=0,
            flag=wx.ALIGN_CENTRE_HORIZONTAL | wx.ALL,
            border=5,
        )

        sizer.Add(
            window=self.upload_btn,
            proportion=0,
            flag=wx.ALIGN_LEFT | wx.ALL,
            border=5,
        )

        sizer.Add(
            window=self.tree_ctrl,
            proportion=1,
            flag=wx.EXPAND | wx.VERTICAL,
            border=5,
        )

        self.SetSizer(sizer)
