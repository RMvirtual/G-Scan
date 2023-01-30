import wx
from src.main.app.display import Display
from src.main.app.main_menu.interface import RootMenu
from src.main.gui import MainMenu

class MainMenuController:
    def __init__(self, application: RootMenu):
        self._app = application
        self._menu = MainMenu(self._app.frame())
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._menu.departments.options.ops.Bind(
            wx.EVT_BUTTON, self._menu.view_ops)

        self._menu.operations.back.Bind(
            wx.EVT_BUTTON, self._menu.view_departments)

        self._bind_root_application_callbacks()

    def _bind_root_application_callbacks(self) -> None:
        self._menu.departments.toolbar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._menu.departments.toolbar.settings.Bind(
            wx.EVT_BUTTON, self.on_settings)

        self._menu.operations.options.cust_pwork.Bind(
            wx.EVT_BUTTON, self.on_customer_paperwork)

        self._menu.operations.options.loading_list.Bind(
            wx.EVT_BUTTON, self.on_loading_list)

    @property
    def panel(self) -> wx.Panel:
        return self._menu

    def show(self) -> None:
        self._menu.Show()

    def hide(self) -> None:
        self._menu.Hide()

    def close(self) -> None:
        self._menu.Close()

    def on_exit(self, event = None) -> None:
        self._app.exit()

    def on_customer_paperwork(self, event = None) -> None:
        self._app.launch_image_viewer()

    def on_loading_list(self, event = None) -> None:
        self._app.launch_image_viewer()

    def on_settings(self, event = None) -> None:
        self._app.launch_settings()