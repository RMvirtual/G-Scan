import wx


class Directories(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Directories, self).__init__(parent=parent)

        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.title = wx.StaticText(parent=self, label="Folders")

        self.scan_label = wx.StaticText(parent=self, label="Scan Directory")
        self.scan_box = wx.TextCtrl(parent=self, value="NULL")
        self.scan_browse = wx.Button(parent=self, label="...")

        self.dest_label = wx.StaticText(
            parent=self, label="Destination Directory")

        self.dest_box = wx.TextCtrl(parent=self, value="NULL")
        self.dest_browse = wx.Button(parent=self, label="...")

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        title_font = wx.Font(wx.FontInfo(pointSize=20).Bold())
        self.title.SetFont(title_font)

        font = wx.Font(wx.FontInfo(pointSize=12))

        items = [
            self.scan_label, self.scan_box, self.scan_browse,
            self.dest_label, self.dest_box, self.dest_browse,
        ]

        for item in items:
            item.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=5, hgap=5)

        alignment = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        align_and_expand = wx.EXPAND|alignment

        sizer.Add(window=self.title, pos=(0, 0), span=(1,3), flag=alignment)
        sizer.Add(window=self.scan_label, pos=(1, 0), flag=alignment)
        sizer.Add(window=self.scan_box, pos=(1, 1), flag=align_and_expand)
        sizer.Add(window=self.scan_browse, pos=(1, 2), flag=alignment)
        sizer.Add(window=self.dest_label, pos=(2, 0), flag=alignment)
        sizer.Add(window=self.dest_box, pos=(2, 1), flag=align_and_expand)
        sizer.Add(window=self.dest_browse, pos=(2, 2), flag=alignment)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)
