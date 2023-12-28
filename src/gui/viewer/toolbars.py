import wx


class BottomToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(BottomToolbar, self).__init__(parent)

        self.exit = wx.Button(self, label="Exit")
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(
            self.exit, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)

        self.SetSizer(sizer)


class FileMenu(wx.MenuBar):
    def __init__(self):
        super().__init__()

        self.file_menu = wx.Menu()

        self.import_files = self.file_menu.Append(
            id=wx.ID_ANY,
            item="&Import Files\tCTRL+I",
            helpString="Import Files"
        )

        self.import_prenamed_files = self.file_menu.Append(
            id=wx.ID_ANY,
            item="&Import Prenamed Files\tCTRL+M",
            helpString="Import files prenamed as the reference to be used"
        )

        self.quit = self.file_menu.Append(
            id=wx.ID_ANY, item='&Quit\tF4',
            helpString="Quit to Main Menu"
        )

        self.Append(self.file_menu, "File")


class UserToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)

        font = wx.Font(wx.FontInfo(pointSize=11))

        label_text = "Please enter job reference:"
        self._input_label = wx.StaticText(self, label=label_text)
        self._input_label.SetFont(font)

        self.reference_box = wx.TextCtrl(self)
        self.reference_box.SetFont(font)
        font = wx.Font(wx.FontInfo(pointSize=9)).Bold()

        self._department_label = wx.StaticText(self, label="Department")
        self._department_label.SetFont(font)
        self.department_box = self._default_combobox()

        self._document_label = wx.StaticText(self, label="Document Type")
        self._document_label.SetFont(font)
        self.document_box = self._default_combobox()

        self.submit = wx.Button(self, label="Submit")

        sizer = wx.GridBagSizer(vgap=0, hgap=0)

        border = 5
        label_flags = wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM

        sizer.Add(
            self._input_label, 
            pos=(0,0), span=(1,2), flag=wx.TOP|label_flags, border=border
        )

        sizer.Add(
            self._department_label, pos=(0,2), flag=label_flags, border=border)

        sizer.Add(
            self._document_label, pos=(0,3), flag=label_flags, border=border)

        flags = wx.ALL

        sizer.Add(self.reference_box, pos=(1, 0), flag=flags, border=border)
        sizer.Add(self.submit, pos=(1,1), flag=flags, border=border)
        sizer.Add(self.department_box, pos=(1,2), flag=flags, border=border)
        sizer.Add(self.document_box, pos=(1,3), flag=flags, border=border)

        self.SetSizer(sizer)

    @property
    def reference_input(self) -> str:
        return self.reference_box.GetValue()

    @reference_input.setter
    def reference_input(self, value: str) -> None:
        self.reference_box.SetValue(value)

    def clear_reference_input(self) -> None:
        self.reference_box.Clear()

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
