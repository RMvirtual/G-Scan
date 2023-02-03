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
        self._initialise_input_box()
        self._initialise_dropdown_boxes()
        self._initialise_buttons()

    def _initialise_input_box(self) -> None:
        font = fonts.font(point_size=11)

        label_text = "Please enter job reference:"
        self._input_label = wx.StaticText(self, label=label_text)
        self._input_label.SetFont(font)

        self._reference_input = wx.TextCtrl(self)
        self._reference_input.SetFont(font)

    def _initialise_dropdown_boxes(self) -> None:
        font = fonts.font(point_size=9, bold=True)

        self._department_label = wx.StaticText(self, label="Department")
        self._department_label.SetFont(font)
        self.department_box = self._default_combobox()

        self._document_label = wx.StaticText(self, label="Document Type")
        self._document_label.SetFont(font)
        self.document_box = self._default_combobox()

    def _initialise_buttons(self) -> None:
        self.submit = wx.Button(self, label="Submit")
        self.skip = wx.Button(self, label="Skip")
        self.split = wx.Button(self, label="Split")

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=0, hgap=0)

        border = 5
        label_flags = wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM

        sizer.Add(
            window=self._input_label,
            pos=(0,0), span=(1,4), flag=wx.TOP|label_flags, border=border
        )

        sizer.Add(
            window=self._department_label,
            pos=(0,4), flag=label_flags, border=border
        )

        sizer.Add(
            window=self._document_label,
            pos=(0,5), flag=label_flags, border=border
        )

        flags = wx.ALL
        sizer.Add(
            window=self._reference_input, pos=(1, 0), flag=flags, border=border)

        sizer.Add(window=self.submit, pos=(1,1), flag=flags, border=border)
        sizer.Add(window=self.skip, pos=(1,2), flag=flags, border=border)
        sizer.Add(window=self.split, pos=(1,3), flag=flags, border=border)

        sizer.Add(
            window=self.department_box, pos=(1, 4), flag=flags, border=border)

        sizer.Add(
            window=self.document_box, pos=(1, 5), flag=flags, border=border)

        self.SetSizer(sizer)

    @property
    def reference_input(self) -> str:
        return self._reference_input.GetValue()

    @reference_input.setter
    def reference_input(self, value: str) -> None:
        self._reference_input.SetValue(value)

    def clear_reference_input(self) -> None:
        self._reference_input.Clear()

    @property
    def department(self) -> str:
        return self.department_box.GetValue()

    @department.setter
    def department(self, new_department: str) -> None:
        self.department_box.SetValue(new_department)

    @property
    def document_type(self) -> str:
        return self.document_box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.document_box.SetValue(new_document_type)

    @property
    def department_options(self) -> str:
        return self.department_box.GetItems()

    @department_options.setter
    def department_options(self, options: list[str]) -> None:
        self.department_box.SetItems(options)
        self.Layout()

    @property
    def document_options(self) -> list[str]:
        return self.document_box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.document_box.SetItems(new_options)
        self.Layout()

    def _default_combobox(self) -> wx.ComboBox:
        return wx.ComboBox(
            parent=self, value="", choices=[""], style=wx.CB_READONLY)
