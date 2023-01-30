import wx
from src.main.app.settings.interface import SettingsInterface
from src.main.gui import Settings


class SettingsController:
    def __init__(self, root_application: SettingsInterface):
        self._app = root_application
        self._settings = Settings(root_application.frame())
        self._initialise_callbacks()
        self._app.set_panel(self._settings)

    def _initialise_callbacks(self) -> None:
        self._settings.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._settings.exit.Bind(wx.EVT_BUTTON, self.on_exit)

    def show(self) -> None:
        self._settings.show()

    def hide(self) -> None:
        self._settings.hide()

    def close(self) -> None:
        self._settings.close()

    @property
    def panel(self) -> wx.Panel:
        return self._settings

    def on_save(self, event = None) -> None:
        self._app.launch_main_menu()

    def on_exit(self,event = None) -> None:
        self._app.launch_main_menu()

    def set_department_options(self, options: list[str]) -> None:
        ...

    def set_paperwork_options(self, options: list[str]) -> None:
        ...

    def set_department(self, option: str) -> None:
        ...

    def set_paperwork_type(self, option: str) -> None:
        ...

    def get_department(self) -> None:
        ...

    def get_paperwork_type(self) -> None:
        ...

    def set_scan_directory(self, directory: str) -> None:
        ...

    def set_dest_directory(self, directory: str) -> None:
        ...

    def get_scan_directory(self) -> str:
        ...

    def get_dest_directory(self) -> str:
        ...
