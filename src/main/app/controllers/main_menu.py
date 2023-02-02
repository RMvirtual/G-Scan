import wx
from src.main.app.configurations import ImageViewerConfiguration
from src.main.app.interfaces import RootInterface
from src.main.gui import MainMenu


class MainMenuController:
    def __init__(self, root_application: RootInterface):
        self._root = root_application
        self._initialise_gui()
        self._initialise_callbacks()
        self._initialise_keyboard_shortcuts()
        self._gui.SetFocus()

    def _initialise_gui(self) -> None:
        self._gui = MainMenu(self._root.window)
        self._root.window.set_panel(self._gui)

    def _initialise_callbacks(self) -> None:
        self._initialise_department_callbacks()
        self._initialise_operations_callbacks()

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

    def _initialise_operations_callbacks(self) -> None:
        panel = self._gui.operations
        btn_press = wx.EVT_BUTTON

        panel.options.cust_pwork.Bind(btn_press, self.on_customer_paperwork)
        panel.options.loading_list.Bind(btn_press, self.on_loading_list)
        panel.back.Bind(btn_press, self._gui.view_departments)

    def _initialise_department_callbacks(self) -> None:
        panel = self._gui.departments
        btn_press = wx.EVT_BUTTON

        panel.options.ops.Bind(btn_press, self._gui.view_ops)
        panel.toolbar.settings.Bind(btn_press, self.on_settings)
        panel.toolbar.exit.Bind(btn_press, self.on_exit)

    def _initialise_keyboard_shortcuts(self) -> None:
        f4_shortcut_id = wx.NewId()
        self._gui.Bind(wx.EVT_MENU, self.on_f4, id=f4_shortcut_id)

        shortcuts = wx.AcceleratorTable([
            (wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id)])

        self._gui.SetAcceleratorTable(shortcuts)

    def on_f4(self, event: wx.EVT_MENU) -> None:
        if self._gui.operations.IsShown():
            self._gui.view_departments()

        else:
            self.launch_exit()

    def on_exit(self, event = None) -> None:
        self.launch_exit()

    def on_settings(self, event = None) -> None:
        self.launch_settings()

    def on_customer_paperwork(self, event = None) -> None:
        config = ImageViewerConfiguration()
        self.launch_image_viewer(config)

    def on_loading_list(self, event = None) -> None:
        config = ImageViewerConfiguration()
        self.launch_image_viewer(config)

    def on_close(self, event = None) -> None:
        self._gui.Destroy()

    def launch_image_viewer(self, config) -> None:
        self._gui.Close()
        self._root.launch_image_viewer(config)

    def launch_settings(self) -> None:
        self._gui.Close()
        self._root.launch_settings()

    def launch_exit(self) -> None:
        self._gui.Close()
        self._root.exit()
