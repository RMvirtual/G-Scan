import threading

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