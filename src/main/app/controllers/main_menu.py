import wx
from src.main.app.controllers.display_interface import DisplayableController
from src.main.gui import MainMenu


class MainMenuController(DisplayableController):
    def __init__(self, parent_window: wx.Frame):
        self._menu = MainMenu(parent_window)
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._menu.departments.options.ops.Bind(
            wx.EVT_BUTTON, self._menu.view_ops)

        self._menu.operations.back.Bind(
            wx.EVT_BUTTON, self._menu.view_departments)

    @property
    def panel(self) -> wx.Panel:
        return self._menu

    def show(self) -> None:
        self._menu.Show()

    def hide(self) -> None:
        self._menu.Hide()

    def close(self) -> None:
        self._menu.Close()

    def bind_exit(self, callback) -> None:
        self._menu.departments.toolbar.exit.Bind(wx.EVT_BUTTON, callback)

    def bind_customer_paperwork(self, callback) -> None:
        self._menu.operations.options.cust_pwork.Bind(wx.EVT_BUTTON, callback)

    def bind_loading_list(self, callback) -> None:
        self._menu.operations.options.loading_list.Bind(wx.EVT_BUTTON, callback)

    def bind_settings(self, callback) -> None:
        self._menu.departments.toolbar.settings.Bind(wx.EVT_BUTTON, callback)
