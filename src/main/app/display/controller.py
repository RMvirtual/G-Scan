import wx
from src.main.gui.window import Window


class DisplayController:
    def __init__(self):
        self._window = Window()

    def frame(self) -> wx.Frame:
        return self._window

    def show(self) -> None:
        self._window.Show()

    def hide(self) -> None:
        self._window.Hide()

    def close(self) -> None:
        self._window.Close()

    def panel(self) -> wx.Panel:
        return self._window.panel

    def set_panel(self, panel: wx.Panel) -> None:
        self._window.panel = panel

    def set_menu_bar(self, menu_bar: wx.MenuBar) -> None:
        self._window.SetMenuBar(menu_bar)
