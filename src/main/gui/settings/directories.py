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

        self.dest_dir_box = wx.TextCtrl(
            parent=self, value="NULL")
        self.dest_dir_browse = wx.Button(parent=self, label="...")

        font = wx.Font(wx.FontInfo(pointSize=12))

        items = [
            self.scan_dir_label, self.scan_dir_box, self.scan_dir_browse,
            self.dest_dir_label, self.dest_dir_box, self.dest_dir_browse,
        ]

        for item in items:
            item.SetFont(font)


    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        sizer.Add(window=self.scan_dir_label, pos=(0,0), flag=wx.EXPAND)
        sizer.Add(window=self.scan_dir_box, pos=(0,1), flag=wx.EXPAND)
        sizer.Add(window=self.scan_dir_browse, pos=(0,2), flag=wx.EXPAND)

        sizer.Add(window=self.dest_dir_label, pos=(1,0), flag=wx.EXPAND)
        sizer.Add(window=self.dest_dir_box, pos=(1,1), flag=wx.EXPAND)
        sizer.Add(window=self.dest_dir_browse, pos=(1,2), flag=wx.EXPAND)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)

        self.SetSizer(sizer)
