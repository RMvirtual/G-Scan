import wx


class DirectoriesPanel(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent=parent)

        self.title = wx.StaticText(self, label="Folders")

        self.scan_dir_label = wx.StaticText(self, label="Input Directory")
        self.scan_dir_entry = wx.TextCtrl(self, value="")
        self.scan_dir_button = wx.Button(self, label="...")

        self.dest_dir_label = wx.StaticText(self, label="Output Directory")
        self.dest_dir_entry = wx.TextCtrl(self, value="")
        self.dest_dir_button = wx.Button(self, label="...")

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        dir_widgets: list[wx.StaticText|wx.TextCtrl|wx.Button] = [
            self.scan_dir_label, self.scan_dir_entry, self.scan_dir_button,
            self.dest_dir_label, self.dest_dir_entry, self.dest_dir_button,
        ]

        for widget in dir_widgets:
            widget.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        # Sizer layout.
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        flags = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        sizer.Add(window=self.title, pos=(0,0), span=(1,3), flag=flags)

        sizer.Add(self.scan_dir_label, pos=(1,0), flag=flags)
        sizer.Add(self.scan_dir_entry, pos=(1,1), flag=wx.EXPAND|flags)
        sizer.Add(self.scan_dir_button, pos=(1,2), flag=flags)

        sizer.Add(self.dest_dir_label, pos=(2,0), flag=flags)
        sizer.Add(self.dest_dir_entry, pos=(2,1), flag=wx.EXPAND|flags)
        sizer.Add(self.dest_dir_button, pos=(2,2), flag=flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

    @property
    def scan_directory(self) -> str:
        return self.scan_dir_entry.GetValue()

    @scan_directory.setter
    def scan_directory(self, directory: str) -> None:
        self.scan_dir_entry.SetValue(directory)

    @property
    def dest_directory(self) -> str:
        return self.dest_dir_entry.GetValue()

    @dest_directory.setter
    def dest_directory(self, directory: str) -> None:
        self.dest_dir_entry.SetValue(directory)
