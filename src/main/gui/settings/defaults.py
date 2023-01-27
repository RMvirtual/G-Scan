import wx


class Defaults(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Defaults, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.title = wx.StaticText(parent=self, label="Defaults")

        self.departments_label = wx.StaticText(
            parent=self, label="Department")

        self.paperwork_label = wx.StaticText(
            parent=self, label="Paperwork Type")

        self.departments = self._default_combobox()
        self.paperwork = self._default_combobox()

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        title_font = wx.Font(wx.FontInfo(pointSize=20).Bold())
        self.title.SetFont(title_font)

        font = wx.Font(wx.FontInfo(pointSize=12))
        self.departments_label.SetFont(font)
        self.paperwork_label.SetFont(font)
        self.departments.SetFont(font)
        self.paperwork.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=15, hgap=30)

        sizer.Add(
            window=self.title, pos=(0,0), span=(1,2), flag=wx.ALIGN_LEFT)

        sizer.Add(
            window=self.departments_label, pos=(1,0), flag=wx.ALIGN_LEFT)

        sizer.Add(window=self.paperwork_label, pos=(1,1), flag=wx.ALIGN_LEFT)

        sizer.Add(
            window=self.departments, pos=(2,0),
            flag=wx.ALIGN_CENTRE_HORIZONTAL
        )

        sizer.Add(
            window=self.paperwork, pos=(2,1), flag=wx.ALIGN_CENTRE_HORIZONTAL)

        self.SetSizer(sizer)

    def _default_combobox(self) -> wx.ComboBox:
        return wx.ComboBox(
            parent=self, value="NULL", choices=["NULL1", "NULL2"])