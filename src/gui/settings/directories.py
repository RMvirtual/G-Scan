import wx


class DirectoriesPanel(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Folders")
        self.output_dir_lbl = wx.StaticText(self, label="Output Directory")
        self.output_dir_entry = wx.TextCtrl(self, value="")
        self.output_dir_btn = wx.Button(self, label="...")

        self.title_lbl.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        widgets: list[wx.TextCtrl] = [
            self.output_dir_lbl, self.output_dir_entry, self.output_dir_btn]

        for widget in widgets:
            widget.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        # Sizer layout.
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        flags = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        sizer.Add(window=self.title_lbl, pos=(0,0), span=(1,3), flag=flags)

        sizer.Add(self.output_dir_lbl, pos=(1,0), flag=flags)
        sizer.Add(self.output_dir_entry, pos=(1,1), flag=wx.EXPAND|flags)
        sizer.Add(self.output_dir_btn, pos=(1,2), flag=flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)
