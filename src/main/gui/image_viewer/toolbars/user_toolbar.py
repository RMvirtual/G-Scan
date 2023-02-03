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
        self.department = self._default_combobox()
        self.document_type = self._default_combobox()


    def _initialise_sizer(self) -> None:
        border = 5
        sizer = wx.GridBagSizer(vgap=0, hgap=0)

        sizer.Add(
            window=self._input_label, pos=(0,0), span=(1,4),
            flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM, border=border
        )

        sizer.Add(
            window=self._department_label, pos=(0,4),
            flag=wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM, border=border
        )

        sizer.Add(
            window=self._document_type_label, pos=(0,5),
            flag=wx.LEFT|wx.RIGHT|wx.ALIGN_BOTTOM, border=border
        )

        sizer.Add(window=self.input, pos=(1,0), flag=wx.ALL, border=border)
        sizer.Add(window=self.submit, pos=(1,1), flag=wx.ALL, border=border)
        sizer.Add(window=self.skip, pos=(1,2), flag=wx.ALL, border=border)
        sizer.Add(window=self.split, pos=(1,3), flag=wx.ALL, border=border)
        sizer.Add(
            window=self.department, pos=(1,4), flag=wx.ALL, border=border)

        sizer.Add(
            window=self.document_type, pos=(1,5), flag=wx.ALL, border=border)

        self.SetSizer(sizer)

    def clear_job_ref_input(self) -> None:
        self.input.Clear()

    def job_ref_input(self) -> str:
        return self.input.GetValue()

    def _default_combobox(self) -> wx.ComboBox:
        result = wx.ComboBox(
            parent=self, value="Test1", choices=["Test1", "Test2"],
            style=wx.CB_READONLY)

        return result