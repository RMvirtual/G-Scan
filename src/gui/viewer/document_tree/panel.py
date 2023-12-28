import wx

from gui.viewer.document_tree.tree import DocumentTreeCtrl


class DocumentTreePanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self._title = wx.StaticText(parent=self, label="Jobs")
        self._title.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

        self.upload_to_fcl = wx.Button(parent=self, label="Upload to FCL")
        self.tree = DocumentTreeCtrl(parent=self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self._title, proportion=0,
            flag=wx.ALIGN_CENTRE_HORIZONTAL|wx.ALL, border=5
        )

        sizer.Add(
            window=self.upload_to_fcl, proportion=0,
            flag=wx.ALIGN_LEFT|wx.ALL, border=5
        )

        sizer.Add(
            window=self.tree, proportion=1,
            flag=wx.EXPAND|wx.VERTICAL, border=5
        )

        self.SetSizer(sizer)
