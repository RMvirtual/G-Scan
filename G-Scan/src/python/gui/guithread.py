import threading
from gui.gui import GUI

class GUI_Thread(threading.Thread):
    """A class for trying to get the GUI class working as a separate
    thread."""

    def __init__(self, gui):
        """Constructor method."""

        threading.Thread.__init__(self)
        self.__gui = gui

    def run(self):
        """The process to run when the thread is started."""

        self.__gui.run()