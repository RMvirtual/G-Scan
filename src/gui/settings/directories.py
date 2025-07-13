import wx


class DirectoriesPanel(wx.Panel):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Folders")
        self.output_dir_lbl = wx.StaticText(self, label="Output Directory")
        self.output_dir_entry = wx.TextCtrl(self, value="")
        self.output_dir_btn = wx.Button(self, label="...")

        # Fonts.
        title_font = wx.Font(wx.FontInfo(pointSize=20)).Bold()
        self.title_lbl.SetFont(title_font)

        size_12_font = wx.Font(wx.FontInfo(pointSize=12))
        self.output_dir_lbl.SetFont(size_12_font)
        self.output_dir_entry.SetFont(size_12_font)
        self.output_dir_btn.SetFont(size_12_font)

        # Sizer layout.
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        flags = wx.ALIGN_LEFT | wx.ALIGN_CENTRE_VERTICAL
        sizer.Add(window=self.title_lbl, pos=(0, 0), span=(1, 3), flag=flags)

        sizer.Add(self.output_dir_lbl, pos=(1, 0), flag=flags)
        sizer.Add(self.output_dir_entry, pos=(1, 1), flag=wx.EXPAND | flags)
        sizer.Add(self.output_dir_btn, pos=(1, 2), flag=flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)
