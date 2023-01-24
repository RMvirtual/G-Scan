from src.main.gui.app import screen_size
import wx

class MainMenu(wx.Frame):
    def __init__(self, title) -> None:
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)

        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

        self._initial_menu = wx.Panel()