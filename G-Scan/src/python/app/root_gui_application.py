import wx
import threading

class RootGuiApplication(wx.App):
    """A root GUI application."""

    def __init__(self):
        """Creates a new thing."""

        super().__init__()

    def main_loop(self):
        """Starts the main loop."""

        this_thread = threading.Thread(target=self.MainLoop)
        this_thread.start()

