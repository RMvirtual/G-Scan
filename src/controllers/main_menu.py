import wx

from configuration import Configuration
from gui.main_menu.main_menu import MainMenu
from gui.window import Window
from root_interface import RootInterface


class MainMenuController:
    def __init__(
            self, root_application: RootInterface,
            app_config: Configuration,
            window: Window
    ) -> None:
        self._root = root_application
        self._config = app_config

        self._gui = MainMenu(window)

        # Could move this out of the constructor maybe??
        window.set_panel(self._gui)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

        depts = self._gui.departments
        ops = self._gui.operations
        accounts = self._gui.credit_control

        # Callbacks.
        widgets_to_handlers = {
            depts.options.ops: self.on_operations,
            depts.options.pods: self.on_credit_control,
            depts.options.quick_start: self.on_quick_start,
            depts.toolbar.settings_btn: self.on_settings,
            depts.toolbar.exit_btn: self.on_exit,
            ops.options.cust_pwork: self.on_customer_paperwork,
            ops.options.loading_list: self.on_loading_list,
            accounts.back: self.on_back_to_departments,
            accounts.options.customer_paperwork_pod: self.on_signed_customer_paperwork,
            accounts.options.signed_pod: self.on_signed_customer_paperwork    
        }

        for widget, handler in widgets_to_handlers.items():
            widget.Bind(wx.EVT_BUTTON, handler)

        f4_shortcut_id = wx.NewId()
        self._gui.Bind(wx.EVT_MENU, self.on_f4, id=f4_shortcut_id)

        self._gui.SetAcceleratorTable(wx.AcceleratorTable([(
            wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id)]))

        self._gui.SetFocus()
    
    def on_f4(self, event: wx.Event) -> None:
        if self._gui.operations.IsShown():
            self._gui.view_departments()

            return

        self.launch_exit()

    def on_back_to_departments(self, event: wx.Event) -> None:
        self._gui.view_departments()
        self._config.department = None

    def on_quick_start(self, event: wx.Event) -> None:
        self.launch_image_viewer()

    def on_operations(self, event: wx.Event) -> None:
        self._config.department = self._config.database.department(
            short_code="ops")
        
        self._gui.view_ops()

    def on_credit_control(self, event: wx.Event) -> None:
        self._config.department = self._config.database.department(
            short_code="pods")

        self._gui.view_credit_control()

    def on_exit(self, event: wx.Event) -> None:
        self.launch_exit()

    def on_settings(self, event: wx.Event) -> None:
        self.launch_settings()

    def on_customer_paperwork(self, event: wx.Event) -> None:
        self._config.document_type = self._config.database.document(
            short_code="customer_paperwork")
       
        self.launch_image_viewer()

    def on_loading_list(self, event: wx.Event) -> None:
        self._config.document_type = self._config.database.document(
            short_code="loading_list")
        
        self.launch_image_viewer()

    def on_signed_pod(self, event: wx.Event) -> None:
        self._config.document_type = self._config.database.document(
            short_code="standard_delivery_note")

        self.launch_image_viewer()

    def on_signed_customer_paperwork(self, event: wx.Event) -> None:
        self._config.document_type = self._config.database.document(
            short_code="customer_paperwork_signed")

        self.launch_image_viewer()

    def on_close(self, event: wx.Event) -> None:
        self._gui.Destroy()

    def launch_image_viewer(self) -> None:
        self._gui.Close()
        self._root.launch_image_viewer(self._config)

    def launch_settings(self) -> None:
        self._gui.Close()
        self._root.launch_settings()

    def launch_exit(self) -> None:
        self._gui.Close()
        self._root.exit()
