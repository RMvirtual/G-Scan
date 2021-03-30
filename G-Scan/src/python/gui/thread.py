import threading
import wx
from gui.mainmenu.main_menu import MainMenu
from gui.settings.settings_menu import SettingsMenu

class GuiThread(threading.Thread):
    """A class for launching a GUI class as a separate
    thread."""

    def __init__(self):
        """Creates a new settings menu thread."""

        threading.Thread.__init__(self)
        self.__setup_complete = threading.Event()

    def run(self):
        """The process to run when the thread is started."""

        self.__gui = MainMenu()
        self.__setup_complete.set()
        print("Exiting in the run function.")

    def close(self):
        """Closes the app."""

        self.__gui.close()
        self.__app.ExitMainLoop()

    def is_setup_complete(self):
        return self.__setup_complete

    def get_gui(self):
        return self.__gui

class SettingsMenuThread(GuiThread):
    """A class for launching the settings menu as it's own self
    contained thread.
    """

    def __init__(self):
        """Creates a new settings menu thread."""

        threading.Thread.__init__(self)
        self.__setup_complete = threading.Event()

    def run(self):
        """The process to run when the thread is started."""

        self.__gui = SettingsMenu()
        self.__setup_complete.set()

    def close(self):
        """Closes the app."""

        self.__gui.close()
        
    def is_setup_complete(self):
        return self.__setup_complete

    def get_gui(self):
        return self.__gui
