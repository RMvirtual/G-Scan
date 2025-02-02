import wx


class DefaultsPanel(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)

        self.title_lbl = wx.StaticText(self, label="Defaults")
        self.departments_lbl = wx.StaticText(self, label="Departments")
        
        self.department_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.document_lbl = wx.StaticText(self, label="Document Type")
        
        self.document_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.title_lbl.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        all_widgets: list[wx.Button|wx.ComboBox] = [
            self.departments_lbl, self.department_box, self.document_lbl, 
            self.document_box
        ]

        font = wx.Font(wx.FontInfo(pointSize=12))

        for widget in all_widgets:
            widget.SetFont(font)

        sizer = wx.GridBagSizer(vgap=15, hgap=30)
        
        left_flag = wx.ALIGN_LEFT
        sizer.Add(self.title_lbl, pos=(0,0), span=(1,2), flag=left_flag)
        sizer.Add(self.departments_lbl, pos=(1,0), flag=left_flag)
        sizer.Add(self.document_lbl, pos=(1,1), flag=left_flag)
            
        centre_flag = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(self.department_box, pos=(2,0), flag=centre_flag)
        sizer.Add(self.document_box, pos=(2,1), flag=centre_flag)

        self.SetSizer(sizer)

    @property
    def department(self) -> str:
        return self.department_box.GetValue()

    @department.setter
    def department(self, new_department: str) -> None:
        self.department_box.SetValue(new_department)

    @property
    def department_options(self) -> str:
        return self.department_box.GetItems()

    @department_options.setter
    def department_options(self, options: list[str]) -> None:
        self.department_box.SetItems(options)

    @property
    def document_type(self) -> str:
        return self.document_box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.document_box.SetValue(new_document_type)

    @property
    def document_options(self) -> list[str]:
        return self.document_box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.document_box.SetItems(new_options)

