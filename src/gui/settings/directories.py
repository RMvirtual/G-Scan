import wx



class DirectoryBrowseBox:
    def __init__(
            self, parent: wx.Panel, label: str, initial_value: str|None = None
    ) -> None:
        self.label = wx.StaticText(parent, label=label)
        self.entry = wx.TextCtrl(parent, value=(initial_value or ""))
        self.button = wx.Button(parent, label="...")
    
    def set_font(self, font: wx.Font) -> None:
        for widget in (self.label, self.entry, self.button):
            widget.SetFont(font)


class DirectoriesPanel(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent=parent)

        self.title = wx.StaticText(self, label="Folders")
        self.scan_box = DirectoryBrowseBox(self, "Scan Directory")
        self.dest_box = DirectoryBrowseBox(self, "Destination Directory")      

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        for box in self.scan_box, self.dest_box:
            box.set_font(wx.Font(wx.FontInfo(pointSize=12)))

        flags = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        sizer.Add(window=self.title, pos=(0,0), span=(1,3), flag=flags)

        for row_no, box in enumerate((self.scan_box, self.dest_box), start=1):
            sizer.Add(window=box.label, pos=(row_no, 0), flag=flags)
            sizer.Add(window=box.entry, pos=(row_no, 1), flag=wx.EXPAND|flags)
            sizer.Add(window=box.button, pos=(row_no, 2), flag=flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

    @property
    def scan_directory(self) -> str:
        return self.scan_box.entry.GetValue()

    @scan_directory.setter
    def scan_directory(self, directory: str) -> None:
        self.scan_box.entry.SetValue(directory)

    @property
    def dest_directory(self) -> str:
        return self.dest_box.entry.GetValue()

    @dest_directory.setter
    def dest_directory(self, directory: str) -> None:
        self.dest_box.entry.SetValue(directory)
