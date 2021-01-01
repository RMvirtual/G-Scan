import wx

class SettingsWindowGUI():
    """GUI for viewing and amending the user's settings."""

    def __init__(self, main_application):
        """Constructor method."""

        self.__main_application = main_application
        self.__current_user = self.__main_application.get_current_user()

    def run(self):
        """The method to run when this object is passed
        to a thread."""
        self.__app = wx.App(False)
        self.__create_widgets()
        self.__app.MainLoop()
    
    def __create_widgets(self):
        """Creates the widgets required for the settings GUI."""

        self.__frame = wx.Frame(
            None,
            size = (820, 220),
            title = "User Settings: " + self.__current_user.get_name() 
        )

        self.__frame.SetBackgroundColour("WHITE")
    
        self.__frame.Show()