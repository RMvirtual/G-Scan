import wx
from src.main.app.controllers.display_interface import DisplayableController
from src.main.gui.window import Window


class WindowController(DisplayableController):
    def __init__(self):
        self.window = Window()

    def show(self) -> None:
        self.window.Show()

    def hide(self) -> None:
        self.window.Hide()

    def close(self) -> None:
        self.window.Close()

    def panel(self) -> wx.Panel:
        return self.window.panel

    def display(self, controller: DisplayableController) -> None:
        self.window.panel = controller.panel



