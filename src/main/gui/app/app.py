import wx


class GuiApplication:
    def __init__(self):
        self._app = wx.App()

    def run(self) -> None:
        self._app.MainLoop()