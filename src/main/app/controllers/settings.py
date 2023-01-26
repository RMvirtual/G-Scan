import wx
from src.main.gui import Settings


class SettingsController:
    def __init__(self):
        self._settings = Settings()

    def show(self) -> None:
        self._settings.show()

    def hide(self) -> None:
        self._settings.hide()

    def close(self) -> None:
        self._settings.close()
