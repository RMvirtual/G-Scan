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
            None,
            size = (866, 548),
            title = "G-Scan"
        )
        
        self.__frame.SetBackgroundColour("WHITE")

        self.__create_panels()

        self.__frame.Show()

    def __create_panels(self):
        """Creates the main panels for widgets to be instantiated in.
        For use with the __create_widgets() method."""
        # Panel for upper half of the GUI
        # (excluding the middle toolbar).
        self.__top_panel = wx.Panel(
            self.__frame,
            size = (850, 250),
            pos = (0, 0)
        )

        self.__top_panel.SetBackgroundColour("PINK")

        # Panel for middle toolbar.
        self.__middle_panel = wx.Panel(
            self.__frame,
            size = (850, 30),
            pos = (0, 250)
        )

        self.__middle_panel.SetBackgroundColour("YELLOW")

        # Panel for bottom half of the GUI
        # (excluding the middle toolbar).
        self.__bottom_panel = wx.Panel(
            self.__frame,
            size = (850, 230),
            pos = (0, 280)
        )

        self.__bottom_panel.SetBackgroundColour("BLUE")