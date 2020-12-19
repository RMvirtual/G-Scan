import wx
import filesystem
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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

        pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
        pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

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
            pos = (0, 265)
        )

        self.__middle_panel.SetBackgroundColour("YELLOW")

        # Panel for bottom half of the GUI
        # (excluding the middle toolbar).
        self.__bottom_panel = wx.Panel(
            self.__frame,
            size = (850, 230),
            pos = (0, 295)
        )

        self.__bottom_panel.SetBackgroundColour("BLUE")

    def __create_top_panel(self):
        """Creates the top panel's sub-panels and corresponding
        widgets."""
        # Panel for upper half of the GUI
        # (excluding the middle toolbar).
        self.__top_panel = wx.Panel(
            self.__frame,
            size = (850, 255),
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
            size = (425, 255),
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

        self.__file_name_label.SetFont(wx.Font(
            14, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # File name value label.
        self.__file_name_text_ctrl = wx.StaticText(
            self.__file_panel,
            label = "I AM A FILE NAME",
            pos = (100, 130),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_name_text_ctrl.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))
        
        self.__file_name_text_ctrl.SetBackgroundColour("LIGHT GREY")

        # File extension label.
        self.__file_extension_label = wx.StaticText(
            self.__file_panel,
            label = "File Type:",
            pos = (0, 160),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_extension_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))
        
        # File extension value label.
        self.__file_extension_value_label = wx.StaticText(
            self.__file_panel,
            label = ".ext",
            pos = (100, 160),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_extension_value_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))
        
        self.__file_extension_value_label.SetBackgroundColour("LIGHT GREY")

        # Input instruction label.
        self.__input_instruction_label = wx.StaticText(
            self.__file_panel,
            label = "Please enter the job reference (excluding \"GR\")",
            pos = (0, 195),
            size = (285, 25),
            style = wx.BORDER_NONE
        )

        self.__input_instruction_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # User input entry box.
        self.__user_input_entry_box = wx.TextCtrl(
            self.__file_panel,
            value = wx.EmptyString,
            pos = (0, 225),
            size = (140, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__user_input_entry_box.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        self.__user_input_entry_box.SetBackgroundColour("LIGHT GREY")
        self.__user_input_entry_box.SetMaxLength(11)

        # Submit button.
        self.__submit_button = wx.Button(
            self.__file_panel,
            label = "Submit",
            size = (60, 25),
            pos = (145, 225))

        self.__submit_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        #self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
         #   self.__submit_button)