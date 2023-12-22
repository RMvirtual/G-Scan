import wx

from gui.departments import Departments, Operations, CreditControl
from gui.logo_panel import Logo


class MainMenu(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.logo = Logo(self)
        self.departments = Departments(self)
        self.operations = Operations(self)
        self.credit_control = CreditControl(self)

        self._subpanels = (
            self.departments, self.operations, self.credit_control)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.logo, proportion=2, flag=wx.EXPAND)

        for panel in self._subpanels:
            sizer.Add(panel, proportion=3, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.WHITE)
        self._switch_to(self.departments)

    def view_departments(self) -> None:
        self._switch_to(self.departments)

    def view_ops(self) -> None:
        self._switch_to(self.operations)

    def view_credit_control(self) -> None:
        self._switch_to(self.credit_control)

    def _switch_to(self, subpanel: wx.Panel) -> None:
        other_panels = filter(
            lambda panel: panel is not subpanel, self._subpanels)
        
        for panel in other_panels:
            panel.Hide()

        subpanel.Show()
        self.Layout()
