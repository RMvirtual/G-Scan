import wx


class Toolbar(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        font_11 = wx.Font(wx.FontInfo(pointSize=11))

        self.input_lbl = wx.StaticText(
            self, label="Please enter job reference:"
        )

        self.input_lbl.SetFont(font_11)

        self.reference_text = wx.TextCtrl(self)
        self.reference_text.SetFont(font_11)

        font_9_bold = wx.Font(wx.FontInfo(pointSize=9)).Bold()
        self.department_lbl = wx.StaticText(self, label="Department")
        self.department_lbl.SetFont(font_9_bold)

        self.department_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        self.document_lbl = wx.StaticText(self, label="Document Type")
        self.document_lbl.SetFont(font_9_bold)

        self.document_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY
        )

        self.submit_btn = wx.Button(self, label="Submit")

        # Grid layout.
        sizer = wx.GridBagSizer(vgap=0, hgap=0)
        centre_bottom = wx.LEFT | wx.RIGHT | wx.ALIGN_BOTTOM

        sizer.Add(
            self.input_lbl, (0, 0), (1, 2), wx.TOP | centre_bottom, border=5
        )

        sizer.Add(
            self.department_lbl, pos=(0, 2), flag=centre_bottom, border=5
        )

        sizer.Add(self.document_lbl, pos=(0, 3), flag=centre_bottom, border=5)
        sizer.Add(self.reference_text, pos=(1, 0), flag=wx.ALL, border=5)
        sizer.Add(self.submit_btn, pos=(1, 1), flag=wx.ALL, border=5)
        sizer.Add(self.department_box, pos=(1, 2), flag=wx.ALL, border=5)
        sizer.Add(self.document_box, pos=(1, 3), flag=wx.ALL, border=5)
        self.SetSizer(sizer)
