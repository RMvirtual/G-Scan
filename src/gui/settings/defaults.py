import wx


class DefaultsPanel(wx.Panel):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Defaults")
        self.department_lbl = wx.StaticText(self, label="Department")

        self.department_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        self.document_lbl = wx.StaticText(self, label="Document Type")

        self.document_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        # Fonts.
        title_font = wx.Font(wx.FontInfo(pointSize=20)).Bold()
        self.title_lbl.SetFont(title_font)

        size_12_font = wx.Font(wx.FontInfo(pointSize=12))
        self.department_lbl.SetFont(size_12_font)
        self.department_box.SetFont(size_12_font)
        self.document_lbl.SetFont(size_12_font)
        self.document_box.SetFont(size_12_font)

        # Sizer layout.
        sizer = wx.GridBagSizer(vgap=15, hgap=30)
        sizer.Add(self.title_lbl, pos=(0, 0), span=(1, 2), flag=wx.ALIGN_LEFT)
        sizer.Add(self.department_lbl, pos=(1, 0), flag=wx.ALIGN_LEFT)
        sizer.Add(self.document_lbl, pos=(1, 1), flag=wx.ALIGN_LEFT)

        sizer.Add(
            self.department_box, pos=(2, 0), flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        sizer.Add(
            self.document_box, pos=(2, 1), flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        self.SetSizer(sizer)
