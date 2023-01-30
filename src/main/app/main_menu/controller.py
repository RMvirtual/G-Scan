import wx
from src.main.app.display import Display
from src.main.app.main_menu.interface import RootMenu
from src.main.gui import MainMenu

class MainMenuController:
    def __init__(self, display: Display, application: RootMenu):
        self._app = application
        self._display = display
        self._menu = MainMenu(self._display.frame())
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._menu.departments.options.ops.Bind(
            wx.EVT_BUTTON, self._menu.view_ops)

        self._menu.operations.back.Bind(
            wx.EVT_BUTTON, self._menu.view_departments)

        self._bind_root_application_callbacks()

    def _bind_root_application_callbacks(self) -> None:
        self.bind_customer_paperwork(self._app.launch_image_viewer)
        self.bind_loading_list(self._app.launch_image_viewer)
        self.bind_settings(self._app.launch_settings)
        self.bind_exit(self._app.exit)

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
