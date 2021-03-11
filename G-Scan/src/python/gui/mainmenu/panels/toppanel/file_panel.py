from app import file_system as filesystem
import wx
from gui.mainmenu.panels.panel import Panel

class FilePanel(Panel):
    """A class modelling the file panel window found in the top panel
    of the main menu GUI.
    """

    def __init__(self, top_panel):
        """Creates a new file panel widget."""

        super().__init__(
            top_panel,
            size = (425, 255),
            position = (0, 0)
        )

        self.__create_widgets()

    def __create_widgets(self):
        """Creates the top-left panel containing the logo,
        file name and type, user input entry box, submit button,
        skip button and split document button."""

        self.__create_logo_widget()
        self.__create_file_detail_widgets()
        self.__create_user_input_widgets()

    def __create_logo_widget(self):
        """Creates the logo in the file panel."""

        gscan_logo_path = (
            filesystem.get_resources_directory() + "images\\g-scan_logo.png")

        logo_image_bitmap = wx.Bitmap(wx.Image(
            gscan_logo_path, wx.BITMAP_TYPE_ANY))
        
        self.__logo_image = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            logo_image_bitmap
        )

    def __create_file_detail_widgets(self):
        """Creates widgets related to displaying details about the
        current file being processed."""

        # File name label.
        self.__file_name_label = wx.StaticText(
            self,
            label = "File Name:",
            pos = (0, 130),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_name_label.SetFont(self.get_body_font())

        # File name value label.
        self.__file_name_text_ctrl = wx.StaticText(
            self,
            label = "I AM A FILE NAME",
            pos = (100, 130),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_name_text_ctrl.SetFont(self.get_body_font())
        self.__file_name_text_ctrl.SetBackgroundColour("LIGHT GREY")

        # File extension label.
        self.__file_extension_label = wx.StaticText(
            self,
            label = "File Type:",
            pos = (0, 160),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_extension_label.SetFont(self.get_body_font())
        
        # File extension value label.
        self.__file_extension_value_label = wx.StaticText(
            self,
            label = ".ext",
            pos = (100, 160),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_extension_value_label.SetFont(self.get_body_font())
        self.__file_extension_value_label.SetBackgroundColour("LIGHT GREY")

    def __create_user_input_widgets(self):
        """Creates widgets related to user input."""

        # Input instruction label.
        self.__input_instruction_label = wx.StaticText(
            self,
            label = "Please enter the job reference (excluding \"GR\")",
            pos = (0, 195),
            size = (285, 25),
            style = wx.BORDER_NONE
        )

        self.__input_instruction_label.SetFont(self.get_body_font())

        # User input entry box.
        self.__user_input_entry_box = wx.TextCtrl(
            self,
            value = wx.EmptyString,
            pos = (0, 225),
            size = (140, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__user_input_entry_box.SetFont(self.get_body_font())
        self.__user_input_entry_box.SetBackgroundColour("LIGHT GREY")
        self.__user_input_entry_box.SetMaxLength(11)

        # Submit button.
        self.__submit_button = wx.Button(
            self,
            label = "Submit",
            size = (60, 25),
            pos = (140, 225))

        self.__submit_button.SetFont(self.get_button_font())

        self.__submit_button.Bind(
            wx.EVT_BUTTON,
            self.__submit_button_click,
            self.__submit_button
        )

        # Skip button.
        self.__skip_button = wx.Button(
            self,
            label = "Skip",
            size = (60, 25),
            pos = (208, 225))

        self.__skip_button.SetFont(self.get_button_font())

        # Split Document button.
        self.__split_document_button = wx.Button(
            self,
            label = "Split Document",
            size = (120, 25),
            pos = (270, 225)
        )

        self.__split_document_button.SetFont(self.get_button_font())

    def __submit_button_click(self, event = None):
        """Defines the behaviour to follow when the submit button
        is clicked, activating the main application's submit
        workflow method."""

        print("Hello")
