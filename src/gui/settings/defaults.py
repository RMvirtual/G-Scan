import wx


class DefaultsPanel(wx.Panel):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Defaults")
        self.depts_lbl = wx.StaticText(self, label="Departments")
        
        self.dept_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.document_lbl = wx.StaticText(self, label="Document Type")
        
        self.doc_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.title_lbl.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        widgets: list[wx.TextCtrl] = [
            self.depts_lbl, self.dept_box, self.document_lbl, self.doc_box]

        font = wx.Font(wx.FontInfo(pointSize=12))

        for widget in widgets:
            widget.SetFont(font)

        # Sizer layout.
        sizer = wx.GridBagSizer(vgap=15, hgap=30)
        sizer.Add(self.title_lbl, pos=(0,0), span=(1,2), flag=wx.ALIGN_LEFT)
        sizer.Add(self.depts_lbl, pos=(1,0), flag=wx.ALIGN_LEFT)
        sizer.Add(self.document_lbl, pos=(1,1), flag=wx.ALIGN_LEFT)
        sizer.Add(self.dept_box, pos=(2,0), flag=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self.doc_box, pos=(2,1), flag=wx.ALIGN_CENTRE_HORIZONTAL)
        self.SetSizer(sizer)
