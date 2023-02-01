import wx
from src.main.app.configurations import ImageViewerConfiguration
from src.main.app.interfaces import RootInterface
from src.main.gui import MainMenu


class MainMenuController:
    def __init__(self, root_application: RootInterface):
        self._root = root_application
        self._initialise_gui()
        self._initialise_callbacks()

    def _initialise_gui(self) -> None:
        self._gui = MainMenu(self._root.window)
        self._root.window.set_panel(self._gui)

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
        self._gui.Close()
        self._root.exit()

    def on_customer_paperwork(self, event = None) -> None:
        config = ImageViewerConfiguration()
        self._gui.close()
        self._root.launch_image_viewer(config)

    def on_loading_list(self, event = None) -> None:
        config = ImageViewerConfiguration()
        self._gui.close()
        self._root.launch_image_viewer(config)

    def on_settings(self, event = None) -> None:
        self._gui.Close()
        self._root.launch_settings()