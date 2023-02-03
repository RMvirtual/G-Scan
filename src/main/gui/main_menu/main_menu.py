import wx
from src.main.gui.main_menu.departments import (
    Departments, Operations, CreditControl)

from src.main.gui.main_menu.logo import Logo


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
        flags = wx.EXPAND

        sizer.Add(window=self.logo, proportion=2, flag=flags, border=0)
        sizer.Add(window=self.departments, proportion=3, flag=flags, border=0)
        sizer.Add(window=self.operations, proportion=3, flag=flags, border=0)
        sizer.Add(
            window=self.credit_control, proportion=3, flag=flags, border=0)

        self.SetSizer(sizer)

    def _switch_to(self, subpanel: wx.Panel) -> None:
        panels_to_hide = [
            panel for panel in self._subpanels if panel is not subpanel]

        for panel in panels_to_hide:
            panel.Hide()

        subpanel.Show()
        self.Layout()

    def view_departments(self) -> None:
        self._switch_to(self.departments)

    def view_ops(self) -> None:
        self._switch_to(self.operations)

    def view_credit_control(self) -> None:
        self._switch_to(self.credit_control)
