import wx


class Defaults(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Defaults, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.departments_label = wx.StaticText(
            parent=self, label="Department")

        self.paperwork_label = wx.StaticText(
            parent=self, label="Paperwork Type")

        self.departments = self._default_combobox()
        self.paperwork = self._default_combobox()

        font = wx.Font(wx.FontInfo(pointSize=14).Bold())

        self.departments_label.SetFont(font)
        self.paperwork_label.SetFont(font)
        self.departments.SetFont(font)
        self.paperwork.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=15, hgap=30)

        sizer.Add(
            window=self.departments_label, pos=(0,0), flag=wx.ALIGN_LEFT)

        sizer.Add(window=self.paperwork_label, pos=(0,1), flag=wx.ALIGN_LEFT)

        sizer.Add(
            window=self.departments, pos=(1,0),
            flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        sizer.Add(
            window=self.paperwork, pos=(1,1), flag=wx.ALIGN_CENTRE_HORIZONTAL)

        self.SetSizer(sizer)

    def _default_combobox(self) -> wx.ComboBox:
        return wx.ComboBox(
            parent=self, value = "NULL", choices=["NULL1", "NULL2"])