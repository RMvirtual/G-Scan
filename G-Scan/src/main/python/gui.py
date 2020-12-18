import wx

class GUI():
    """GUI for running the main application."""

    def __init__(self, main_application):
        """Constructor method."""

        self.__app = wx.App(False)
        self.__main_application = main_application
        self.__create_widgets()
        self.__app.MainLoop()

    def __create_widgets(self):
        """Creates the widgets required for the GUI."""

        # Frame for the entire window.
        self.__frame = wx.Frame(
            None, size = (850, 500), title = "G-Scan")
        
        self.__frame.SetBackgroundColour("White")
        

        
        self.__frame.Show()