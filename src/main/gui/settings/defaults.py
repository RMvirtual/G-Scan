import wx


class Defaults(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Defaults, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.departments = self._default_combobox()
        self.paperwork = self._default_combobox()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.Add(window=self.departments, proportion=0)
        sizer.Add(window=self.paperwork, proportion=0)

        self.SetSizer(sizer)

    def _default_combobox(self) -> wx.ComboBox:
        return wx.ComboBox(
            parent=self, value = "NULL", choices=["NULL1", "NULL2"])