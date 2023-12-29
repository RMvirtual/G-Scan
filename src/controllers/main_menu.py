import wx

from controllers.configuration import AppConfiguration
from controllers.abstract_root import RootInterface
from views import MainMenu


class MainMenuController:
    def __init__(
            self, root_application: RootInterface, app_config: AppConfiguration
    ) -> None:
        self._root = root_application
        self._config = app_config

        self._gui = MainMenu(self._root.window)
        self._root.window.set_panel(self._gui)

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

        depts_panel = self._gui.departments

        dept_options = self._gui.departments.options
        dept_options.ops.Bind(wx.EVT_BUTTON, self.on_operations)
        dept_options.pods.Bind(wx.EVT_BUTTON, self.on_credit_control)
        dept_options.quick_start.Bind(wx.EVT_BUTTON, self.on_quick_start)

        dept_toolbar =  depts_panel.toolbar
        dept_toolbar.settings.Bind(wx.EVT_BUTTON, self.on_settings)
        dept_toolbar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        ops_panel = self._gui.operations
        ops_panel.back.Bind(wx.EVT_BUTTON, self.on_back_to_departments)

        ops_options = ops_panel.options
        ops_options.cust_pwork.Bind(wx.EVT_BUTTON, self.on_customer_paperwork)
        ops_options.loading_list.Bind(wx.EVT_BUTTON, self.on_loading_list)
        
        cc_panel = self._gui.credit_control
        cc_panel.back.Bind(wx.EVT_BUTTON, self.on_back_to_departments)

        cc_options = cc_panel.options
        cc_options.customer_paperwork_pod.Bind(
            wx.EVT_BUTTON, self.on_signed_customer_paperwork)

        cc_options.signed_pod.Bind(wx.EVT_BUTTON, self.on_signed_pod)

        f4_shortcut_id = wx.NewId()
        self._gui.Bind(wx.EVT_MENU, self.on_f4, id=f4_shortcut_id)

        self._gui.SetAcceleratorTable(wx.AcceleratorTable([(
            wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id)]))

        self._gui.SetFocus()

    def on_f4(self, event: wx.EVT_MENU) -> None:
        if self._gui.operations.IsShown():
            self._gui.view_departments()

            return

        self.launch_exit()

    def on_back_to_departments(self, event: wx.EVT_BUTTON) -> None:
        self._gui.view_departments()
        self._config.department = None

    def on_quick_start(self, event: wx.EVT_BUTTON) -> None:
        self.launch_image_viewer(self._config)

    def on_operations(self, event: wx.EVT_BUTTON) -> None:
        self._config.department = self._config.database.department(
            short_code="ops")
        
        self._gui.view_ops()

    def on_credit_control(self, event: wx.EVT_BUTTON) -> None:
        self._config.department = self._config.database.department(
            short_code="pods")

        self._gui.view_credit_control()

    def on_exit(self, event: wx.EVT_BUTTON) -> None:
        self.launch_exit()

    def on_settings(self, event: wx.EVT_BUTTON) -> None:
        self.launch_settings()

    def on_customer_paperwork(self, event: wx.EVT_BUTTON) -> None:
        self._config.document_type = self._config.database.document(
            short_code="customer_paperwork")

        self.launch_image_viewer(self._config)

    def on_loading_list(self, event: wx.EVT_BUTTON) -> None:
        self._config.document_type = self._config.database.document(
            short_code="loading_list")
        
        self.launch_image_viewer(self._config)

    def on_signed_pod(self, event: wx.EVT_BUTTON) -> None:
        self._config.document_type = self._config.database.document(
            short_code="standard_delivery_note")

        self.launch_image_viewer(self._config)

    def on_signed_customer_paperwork(self, event: wx.EVT_BUTTON) -> None:
        self._config.document_type = self._config.database.document(
            short_code="customer_paperwork_signed")

        self.launch_image_viewer(self._config)

    def on_close(self, event: wx.EVT_BUTTON = None) -> None:
        self._gui.Destroy()

    def launch_image_viewer(self, config) -> None:
        self._gui.Close()
        self._root.launch_image_viewer(self._config)

    def launch_settings(self) -> None:
        self._gui.Close()
        self._root.launch_settings()

    def launch_exit(self) -> None:
        self._gui.Close()
        self._root.exit()
