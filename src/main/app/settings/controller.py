import wx
from src.main.app.display import Display
from src.main.gui import Settings


class SettingsController:
    def __init__(self, window: Display):
        self._settings = Settings(window.frame())

    def show(self) -> None:
        self._settings.show()

    def hide(self) -> None:
        self._settings.hide()

    def close(self) -> None:
        self._settings.close()

    @property
    def panel(self) -> wx.Panel:
        return self._settings

    def bind_save_button(self, callback) -> None:
        self._settings.save.Bind(wx.EVT_BUTTON, callback)

    def bind_exit_button(self, callback) -> None:
        self._settings.exit.Bind(wx.EVT_BUTTON, callback)

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
