import wx
from src.main.app.controllers.display_interface import DisplayableController
from src.main.gui import Settings


class SettingsController(DisplayableController):
    def __init__(self, window: wx.Frame):
        self._settings = Settings(window)

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
