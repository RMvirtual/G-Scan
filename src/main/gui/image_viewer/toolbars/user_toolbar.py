import wx
from src.main.gui import fonts


class UserToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise()

    def _initialise(self) -> None:
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self._input_label = wx.StaticText(
            self, label="Please enter job reference:")

        self._input_label.SetFont(fonts.font(point_size=11))

        self._department_label = wx.StaticText(self, label="Department")
        self._department_label.SetFont(fonts.font(point_size=9, bold=True))

        self._document_type_label = wx.StaticText(self, label="Document Type")
        self._document_type_label.SetFont(fonts.font(point_size=9, bold=True))

        self.input = wx.TextCtrl(self)
        self.submit = wx.Button(self, label="Submit")
        self.skip = wx.Button(self, label="Skip")
        self.split = wx.Button(self, label="Split")
        self.department_box = self._default_combobox()
        self.document_type_box = self._default_combobox()


    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=0, hgap=0)

        border = 5
        row_0_flags = wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM

        sizer.Add(
            window=self._input_label, pos=(0,0), span=(1,4),
            flag=wx.TOP|row_0_flags, border=border
        )

        sizer.Add(
            window=self._department_label, pos=(0,4),
            flag=row_0_flags, border=border
        )

        sizer.Add(
            window=self._document_type_label, pos=(0,5),
            flag=row_0_flags, border=border
        )

        sizer.Add(window=self.input, pos=(1,0), flag=wx.ALL, border=border)
        sizer.Add(window=self.submit, pos=(1,1), flag=wx.ALL, border=border)
        sizer.Add(window=self.skip, pos=(1,2), flag=wx.ALL, border=border)
        sizer.Add(window=self.split, pos=(1,3), flag=wx.ALL, border=border)

        sizer.Add(
            window=self.department_box, pos=(1, 4), flag=wx.ALL, border=border)

        sizer.Add(
            window=self.document_type_box, pos=(1, 5), flag=wx.ALL, border=border)

        self.SetSizer(sizer)

    def clear_job_ref_input(self) -> None:
        self.input.Clear()

    def job_ref_input(self) -> str:
        return self.input.GetValue()

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
        return self.document_type_box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.document_type_box.SetValue(new_document_type)

    @property
    def document_options(self) -> list[str]:
        return self.document_type_box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.document_type_box.SetItems(new_options)

    def _default_combobox(self) -> wx.ComboBox:
        result = wx.ComboBox(
            parent=self, value="Test1", choices=["Test1", "Test2"],
            style=wx.CB_READONLY
        )

        return result