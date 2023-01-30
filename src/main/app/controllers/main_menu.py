import wx
from src.main.app.root.interface import RootInterface
from src.main.gui import MainMenu


class MainMenuController:
    def __init__(self, root_application: RootInterface):
        self._app = root_application
        self._gui = MainMenu(self._app.frame())
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._gui.departments.options.ops.Bind(
            wx.EVT_BUTTON, self._gui.view_ops)

        self._gui.operations.back.Bind(
            wx.EVT_BUTTON, self._gui.view_departments)

        self._bind_root_application_callbacks()

    def _bind_root_application_callbacks(self) -> None:
        self._gui.departments.toolbar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._gui.departments.toolbar.settings.Bind(
            wx.EVT_BUTTON, self.on_settings)

        self._gui.operations.options.cust_pwork.Bind(
            wx.EVT_BUTTON, self.on_customer_paperwork)

        self._gui.operations.options.loading_list.Bind(
            wx.EVT_BUTTON, self.on_loading_list)

    @property
    def panel(self) -> wx.Panel:
        return self._gui

    def close(self) -> None:
        self._gui.Close()

    def on_exit(self, event = None) -> None:
        self._app.exit()

    def on_customer_paperwork(self, event = None) -> None:
        self._app.launch_image_viewer()

    def on_loading_list(self, event = None) -> None:
        self._app.launch_image_viewer()

    def on_settings(self, event = None) -> None:
        self._app.launch_settings()