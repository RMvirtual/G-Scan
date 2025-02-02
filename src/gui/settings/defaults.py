import wx


class DropDownOption:
    def __init__(self, parent: wx.Panel, label: str) -> None:
        self.label = wx.StaticText(parent, label=label)
        
        self.box = wx.ComboBox(
            parent, value="", choices=[""], style=wx.CB_READONLY)

    def set_font(self, font: wx.Font) -> None:
        self.label.SetFont(font)
        self.box.SetFont(font)


class DefaultsPanel(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)

        self.title = wx.StaticText(self, label="Defaults")
        self.department_option = DropDownOption(self, "Departments")
        self.document_option = DropDownOption(self, "Document Type")

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        for box in self.department_option, self.document_option:
            box.set_font(wx.Font(wx.FontInfo(pointSize=12)))

        sizer = wx.GridBagSizer(vgap=15, hgap=30)
        
        left_flag = wx.ALIGN_LEFT
        sizer.Add(self.title, pos=(0,0), span=(1,2), flag=left_flag)
        sizer.Add(self.department_option.label, pos=(1,0), flag=left_flag)
        sizer.Add(self.document_option.label, pos=(1,1), flag=left_flag)
            
        centre_flag = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(self.department_option.box, pos=(2,0), flag=centre_flag)
        sizer.Add(self.document_option.box, pos=(2,1), flag=centre_flag)

        self.SetSizer(sizer)

    @property
    def department(self) -> str:
        return self.department_option.box.GetValue()

    @department.setter
    def department(self, new_department: str) -> None:
        self.department_option.box.SetValue(new_department)

    @property
    def department_options(self) -> str:
        return self.department_option.box.GetItems()

    @department_options.setter
    def department_options(self, options: list[str]) -> None:
        self.department_option.box.SetItems(options)

    @property
    def document_type(self) -> str:
        return self.document_option.box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.document_option.box.SetValue(new_document_type)

    @property
    def document_options(self) -> list[str]:
        return self.document_option.box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.document_option.box.SetItems(new_options)

