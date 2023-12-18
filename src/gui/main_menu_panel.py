import wx

from gui.departments import Departments, Operations, CreditControl
from gui.logo_panel import Logo


class MainMenu(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent=parent)

        self._initialise_panels()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.WHITE)
        self._switch_to(self.departments)

    def _initialise_panels(self) -> None:
        self.logo = Logo(self)
        self.departments = Departments(self)
        self.operations = Operations(self)
        self.credit_control = CreditControl(self)

        self._subpanels = (
            self.departments, self.operations, self.credit_control)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self.logo, proportion=2, flag=wx.EXPAND)

        for panel in self._subpanels:
            sizer.Add(window=panel, proportion=3, flag=wx.EXPAND)

        self.SetSizer(sizer)

    def view_departments(self) -> None:
        self._switch_to(self.departments)

    def view_ops(self) -> None:
        self._switch_to(self.operations)

    def view_credit_control(self) -> None:
        self._switch_to(self.credit_control)

    def _switch_to(self, subpanel: wx.Panel) -> None:
        self._hide_complement_of(subpanel)
        subpanel.Show()
        self.Layout()

    def _hide_complement_of(self, subpanel: wx.Panel) -> None:
        for panel in self._complement_of(subpanel):
            panel.Hide()

    def _complement_of(self, subpanel) -> list[wx.Panel]:
        return filter(lambda panel: panel is not subpanel, self._subpanels)
