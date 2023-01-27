import wx
from src.main.gui.window import Window


class WindowController:
    def __init__(self,) -> None:
        self.window = Window()

    def show(self) -> None:
        self.window.Show()

    def hide(self) -> None:
        self.window.Hide()

    def close(self) -> None:
        self.window.Close()

    def set_panel(self, panel: wx.Panel) -> None:
        self.window.panel = panel

    def refresh(self) -> None:
        self.window.Refresh()