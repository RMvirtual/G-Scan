import wx


class Directories(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Directories, self).__init__(parent=parent)

        self._initialise_widgets()
        self._initialise_sizer()

        self.SetBackgroundColour(wx.BLUE)

    def _initialise_widgets(self) -> None:
        self.scan_dir_label = wx.StaticText(
            parent=self, label="Scan Directory")

        self.scan_dir_box = wx.TextCtrl(parent=self, value="NULL")
        self.scan_dir_browse = wx.Button(parent=self, label="...")

        self.dest_dir_label = wx.StaticText(
            parent=self, label="Destination Directory")

        self.dest_dir_box = wx.TextCtrl(parent=self, value="NULL")
        self.dest_dir_browse = wx.Button(parent=self, label="...")

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=12))

        items = [
            self.scan_dir_label, self.scan_dir_box, self.scan_dir_browse,
            self.dest_dir_label, self.dest_dir_box, self.dest_dir_browse,
        ]

        for item in items:
            item.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=5, hgap=5)

        alignment_flags = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        align_and_expand = wx.EXPAND|alignment_flags

        sizer.Add(window=self.scan_dir_label, pos=(0,0), flag=alignment_flags)
        sizer.Add(window=self.scan_dir_box, pos=(0,1), flag=align_and_expand)
        sizer.Add(window=self.scan_dir_browse, pos=(0,2), flag=alignment_flags)
        sizer.Add(window=self.dest_dir_label, pos=(1,0), flag=alignment_flags)
        sizer.Add(window=self.dest_dir_box, pos=(1,1), flag=align_and_expand)
        sizer.Add(window=self.dest_dir_browse, pos=(1,2), flag=alignment_flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)
