import wx
from src.main.gui import fonts


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
        self._initialise_title_font()
        self._initialise_body_font()

    def _initialise_title_font(self) -> None:
        self.title.SetFont(fonts.font(point_size=20, bold=True))

    def _initialise_body_font(self) -> None:
        font = fonts.font(point_size=12)

        widgets = [
            self.departments_label, self.paperwork_label,
            self.departments, self.paperwork
        ]

        for widget in widgets:
            widget.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.GridBagSizer(vgap=15, hgap=30)

        sizer.Add(window=self.title, pos=(0,0), span=(1,2), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.departments_label, pos=(1,0), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.paperwork_label, pos=(1,1), flag=wx.ALIGN_LEFT)

        align_centre = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(window=self.departments, pos=(2,0), flag=align_centre)
        sizer.Add(window=self.paperwork, pos=(2,1), flag=align_centre)

        self.SetSizer(sizer)

    def _default_combobox(self) -> wx.ComboBox:
        dummy_values = ["NULL", "NULL2"]

        return wx.ComboBox(parent=self, value="NULL", choices=dummy_values)
