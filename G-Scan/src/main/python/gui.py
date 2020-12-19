import wx
import filesystem

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

        self.__create_top_panel()

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

    def __create_top_panel(self):
        """Creates the top panel's sub-panels and corresponding
        widgets."""
        # Panel for upper half of the GUI
        # (excluding the middle toolbar).
        self.__top_panel = wx.Panel(
            self.__frame,
            size = (850, 250),
            pos = (10, 10)
        )

        self.__top_panel.SetBackgroundColour("PINK")
        self.__create_file_panel()

    def __create_file_panel(self):
        """Creates the top-left panel containing the logo,
        file name and type, user input entry box, submit button,
        skip button and split document button."""

        # File panel to contain all the widgets.
        self.__file_panel = wx.Panel(
            self.__top_panel,
            size = (425, 250),
            pos = (0, 0)
        )

        # self.__file_panel.SetBackgroundColour("White")

        # Logo image.
        gscan_logo_path = (
            filesystem.get_resources_directory() + "images\\g-scan_logo.png")

        logo_image_bitmap = wx.Bitmap(wx.Image(gscan_logo_path, wx.BITMAP_TYPE_ANY))
        
        self.__logo_image = wx.StaticBitmap(
            self.__file_panel,
            wx.ID_ANY,
            logo_image_bitmap
        )

        # File name label.
        self.__file_name_label = wx.StaticText(
            self.__file_panel,
            label = "File Name:",
            pos = (0, 130),
            size = (70, 20),
            style = wx.BORDER_NONE
        )
        
        # File extension label.
        self.__file_extension_label = wx.StaticText(
            self.__file_panel,
            label = "File Type:",
            pos = (0, 150),
            size = (70, 20),
            style = wx.BORDER_NONE
        )