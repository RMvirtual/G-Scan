import wx
from gui import fonts


class Defaults(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Defaults, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.title = self._title_label("Defaults")
        self.departments_label = self._default_label("Departments")
        self.doc_type_label = self._default_label("Document Type")
        self.department_box = self._default_combobox()
        self.doc_type_box = self._default_combobox()

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=15, hgap=30)

        sizer.Add(window=self.title, pos=(0,0), span=(1,2), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.departments_label, pos=(1,0), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.doc_type_label, pos=(1, 1), flag=wx.ALIGN_LEFT)

        align_centre = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(window=self.department_box, pos=(2, 0), flag=align_centre)
        sizer.Add(window=self.doc_type_box, pos=(2, 1), flag=align_centre)

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
        return self.doc_type_box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.doc_type_box.SetValue(new_document_type)

    @property
    def document_options(self) -> list[str]:
        return self.doc_type_box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.doc_type_box.SetItems(new_options)

    def _title_label(self, value: str) -> wx.StaticText:
        result = wx.StaticText(parent=self, label=value)
        result.SetFont(fonts.font(point_size=20, bold=True))

        return result

    def _default_label(self, value: str) -> wx.StaticText:
        result =  wx.StaticText(parent=self, label=value)
        result.SetFont(font=fonts.font(point_size=12))

        return result

    def _default_combobox(self) -> wx.ComboBox:
        result = wx.ComboBox(
            parent=self, value="", choices=[""], style=wx.CB_READONLY)

        result.SetFont(font=fonts.font(point_size=12))

        return result