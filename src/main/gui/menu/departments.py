import wx
from src.main.gui.menu.settings_toolbar import SettingsToolbar


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

        sizer.Add(window=self.toolbar, flag=wx.ALIGN_RIGHT)

        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(DepartmentOptions, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizer()

    def _initialise_buttons(self) -> None:
        self.ops = wx.Button(parent=self, label="Ops")
        self.pods = wx.Button(parent=self, label="PODs")

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        for button in [self.ops, self.pods]:
            button.SetFont(font)

    def _initialise_sizer(self) -> None:
        flags = wx.ALL|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddStretchSpacer()

        sizer.Add(window=self.ops, proportion=0, flag=flags, border=border)
        sizer.Add(window=self.pods, proportion=0, flag=flags, border=border)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)
