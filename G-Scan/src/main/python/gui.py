import wx

class GUI():
    """GUI for running the main application."""

    def __init__(self, main_application):
        """Constructor method."""

        self.__app = wx.App(False)
        self.__main_application = main_application
        