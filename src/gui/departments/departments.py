import wx

from gui import fonts
from gui.departments.bottom_toolbar import SettingsToolbar


class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Departments, self).__init__(parent)
        self._initialise_panels()
        self._initialise_sizer()

    def _initialise_panels(self) -> None:
        self.options = DepartmentOptions(self)
        self.toolbar = SettingsToolbar(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(window=self.toolbar, proportion=0, flag=wx.ALIGN_RIGHT)

        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(DepartmentOptions, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizer()

    def _initialise_buttons(self) -> None:
        self.ops = wx.Button(parent=self, label="Ops")
        self.pods = wx.Button(parent=self, label="PODs")
        self.quick_start = wx.Button(parent=self, label="Quick Start")

        self.buttons = [self.ops, self.pods, self.quick_start]

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self.buttons:
            button.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in self.buttons:
            sizer.Add(
                window=button, proportion=0,
                flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, border=15
            )

        self.SetSizer(sizer)
