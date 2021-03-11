import threading
from gui.main_menu.main_menu import MainMenu

class MainMenuThread(threading.Thread):
    """A class for trying to get the GUI class working as a separate
    thread."""

    def __init__(self, main_menu):
        """Constructor method."""

        threading.Thread.__init__(self)
        self.__main_menu = main_menu

    def run(self):
        """The process to run when the thread is started."""

        self.__main_menu.run()