import datetime

import wx


class JobEntryToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        font_9_bold = wx.Font(wx.FontInfo(pointSize=9)).Bold()
        self.input_lbl = wx.StaticText(self, label="Job Reference")
        self.input_lbl.SetFont(font_9_bold)

        self.reference_input = wx.TextCtrl(self)
        self.submit_btn = wx.Button(self, label="Submit")
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

        current_date = datetime.date.today()

        self.month_box = wx.ComboBox(
            self,
            choices=list(map(lambda m: str(m).zfill(2), range(1, 13))),
            value=current_date.strftime("%m"),
            style=wx.CB_READONLY,
        )

        last_year = current_date.replace(current_date.year - 1)

        year_options = [
            last_year.strftime("%Y"),
            current_date.strftime("%Y"),
        ]

        self.year_box = wx.ComboBox(
            self,
            choices=year_options,
            value=current_date.strftime("%Y"),
            style=wx.CB_READONLY,
        )

        # Grid layout.
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        sizer.Add(self.input_lbl, (0, 0), (1, 2))
        sizer.Add(self.department_lbl, pos=(0, 2))
        sizer.Add(self.document_lbl, pos=(0, 3))

        sizer.Add(self.reference_input, (1, 0), (1, 2), wx.EXPAND)
        sizer.Add(self.submit_btn, pos=(1, 2))
        sizer.Add(self.department_box, pos=(1, 3))
        sizer.Add(self.document_box, pos=(1, 4))

        sizer.Add(self.month_box, pos=(2, 0))
        sizer.Add(self.year_box, pos=(2, 1))
        self.SetSizer(sizer)
