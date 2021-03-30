import threading
import wx

from gui.settings.settings_menu import SettingsMenu

class GuiThread(threading.Thread):
    """A class for launching a GUI class as a separate
    thread."""

    def __init__(self, gui):
        """Creates a new GUI thread. Requires the gui element to have a
        run() method containing the behaviour required to run when the
        thread is started."""

        threading.Thread.__init__(self)
        self.__gui = gui

    def run(self):
        """The process to run when the thread is started."""

        self.__gui.run()

class SettingsMenuThread(threading.Thread):
    """A class for launching the settings menu as it's own self
    contained thread.
    """

    def __init__(self, main_application):
        """Creates a new settings menu thread."""

        threading.Thread.__init__(self)
        self.__main_application = main_application
        self.__setup_complete = threading.Event()

    def run(self):
        """The process to run when the thread is started."""

        self.__app = wx.App()
        self.__gui = SettingsMenu(self.__main_application)
        self.__setup_complete.set()
        self.__app.MainLoop()

    def close(self):
        """Closes the app."""

        self.__app.ExitMainLoop()
        self.__app.Destroy()

    def is_setup_complete(self):
        return self.__setup_complete

    def get_settings_menu(self):
        return self.__gui
