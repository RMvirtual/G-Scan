import wx
from src.main.gui.window import Window


class DisplayController:
    def __init__(self):
        self._window = Window()

    @property
    def window(self) -> Window:
        return self._window

    def show(self) -> None:
        self._window.Show()

    def hide(self) -> None:
        self._window.Hide()

    def close(self) -> None:
        self._window.Close()
