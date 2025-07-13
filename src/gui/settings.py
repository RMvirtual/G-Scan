import wx


class Settings(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Settings")

        self.output_directory_lbl = wx.StaticText(
            self, label="Output Directory"
        )

        self.output_directory_entry = wx.TextCtrl(self, value="")
        self.output_directory_btn = wx.Button(self, label="...")
        self.defaults_lbl = wx.StaticText(self, label="Defaults")
        self.department_lbl = wx.StaticText(self, label="Department")

        self.department_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        self.document_lbl = wx.StaticText(self, label="Document Type")

        self.document_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        self.save_btn = wx.Button(self, label="Save")
        self.exit_btn = wx.Button(self, label="Exit")

        # Fonts.
        title_font = wx.Font(wx.FontInfo(pointSize=30)).Bold()
        self.title_lbl.SetFont(title_font)

        heading_font = wx.Font(wx.FontInfo(pointSize=20)).Bold()
        self.defaults_lbl.SetFont(heading_font)

        size_12_font = wx.Font(wx.FontInfo(pointSize=12))
        self.output_directory_lbl.SetFont(size_12_font)
        self.output_directory_entry.SetFont(size_12_font)
        self.output_directory_btn.SetFont(size_12_font)
        self.department_lbl.SetFont(size_12_font)
        self.department_box.SetFont(size_12_font)
        self.document_lbl.SetFont(size_12_font)
        self.document_box.SetFont(size_12_font)
        self.save_btn.SetFont(size_12_font)
        self.exit_btn.SetFont(size_12_font)

        # Sizer layout.
        output_directory_sizer = wx.GridBagSizer(vgap=5, hgap=5)

        output_directory_sizer.Add(
            self.output_directory_lbl,
            pos=(1, 0),
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTRE_VERTICAL,
        )

        output_directory_sizer.Add(
            self.output_directory_entry,
            pos=(1, 1),
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTRE_VERTICAL | wx.EXPAND,
        )

        output_directory_sizer.AddGrowableCol(1)

        output_directory_sizer.Add(
            self.output_directory_btn,
            pos=(1, 2),
            flag=wx.ALIGN_LEFT | wx.ALIGN_CENTRE_VERTICAL,
        )

        defaults_sizer = wx.GridBagSizer(vgap=15, hgap=30)
        defaults_sizer.Add(self.defaults_lbl, (0, 0), (1, 2), wx.ALIGN_LEFT)
        defaults_sizer.Add(self.department_lbl, pos=(1, 0), flag=wx.ALIGN_LEFT)
        defaults_sizer.Add(self.document_lbl, pos=(1, 1), flag=wx.ALIGN_LEFT)

        defaults_sizer.Add(
            self.department_box, pos=(2, 0), flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        defaults_sizer.Add(
            self.document_box, pos=(2, 1), flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        main_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        border = 15

        main_sizer.Add(self.title_lbl, 0, wx.ALIGN_LEFT | wx.ALL, border)
        main_sizer.Add(output_directory_sizer, 0, wx.EXPAND | wx.ALL, border)
        main_sizer.Add(defaults_sizer, 0, wx.ALIGN_LEFT | wx.ALL, border)

        align_bottom_right = wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM
        main_sizer.Add(self.save_btn, 0, align_bottom_right, border)
        main_sizer.Add(self.exit_btn, 0, align_bottom_right, border)
        main_sizer.AddStretchSpacer()

        self.SetSizer(main_sizer)
        self.SetBackgroundColour(colour=wx.WHITE)
