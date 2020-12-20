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
        self.__create_middle_panel()
        self.__create_bottom_panel()

    def __create_top_panel(self):
        """Creates the top panel's sub-panels and corresponding
        widgets."""
        # Panel for upper half of the GUI
        # (excluding the middle toolbar).
        self.__top_panel = wx.Panel(
            self.__frame,
            size = (840, 255),
            pos = (10, 10)
        )

        self.__top_panel.SetBackgroundColour("PINK")
        self.__create_file_panel()
        self.__create_user_settings_panel()

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

        self.__file_panel.SetBackgroundColour("WHITE")

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
            pos = (140, 225))

        self.__submit_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        #self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
         #   self.__submit_button)

        # Skip button.
        self.__skip_button = wx.Button(
            self.__file_panel,
            label = "Skip",
            size = (60, 25),
            pos = (208, 225))

        self.__skip_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Split Document button.
        self.__split_document_button = wx.Button(
            self.__file_panel,
            label = "Split Document",
            size = (120, 25),
            pos = (270, 225)
        )

        self.__split_document_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_user_settings_panel(self):
        """Creates the user settings panel in the top right of the
        GUI."""

        # User settings panel to contain all the user settings,
        # file handling and mode widgets.
        self.__user_settings_panel = wx.Panel(
            self.__top_panel,
            size = (420, 255),
            pos = (425, 0)
        )

        self.__user_settings_panel.SetBackgroundColour("WHITE")

        # Paperwork type heading label.
        self.__paperwork_type_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Paperwork Type",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__paperwork_type_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # "Customer Paperwork" paperwork type radio button.
        self.__customer_paperwork_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Customer Paperwork",
            size = (160, 25),
            pos = (0, 25),
            style = wx.RB_GROUP
        )

        self.__customer_paperwork_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # "Loading List" paperwork type radio button.
        self.__loading_list_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Loading List",
            size = (90, 25),
            pos = (160, 25),
        )

        self.__loading_list_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # "POD" paperwork type radio button.
        self.__pod_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "POD",
            size = (45, 25),
            pos = (265, 25)
        )

        self.__pod_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = wx.CheckBox(
            self.__user_settings_panel,
            label = "Autoprocess",
            size = (85, 25),
            pos = (320, 25)
        )

        self.__autoprocessing_checkbox.SetFont(wx.Font(
            9, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Input Mode heading label.
        self.__input_mode_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Input Mode",
            size = (60, 25),
            pos = (0, 75)
        )

        self.__input_mode_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Normal Mode radio button.
        self.__normal_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Normal Mode",
            size = (120, 25),
            pos = (0, 100),
            style = wx.RB_GROUP
        )

        self.__normal_mode_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Quick Mode radio button.
        self.__quick_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Quick Mode",
            size = (90, 25),
            pos = (160, 100),
        )

        self.__quick_mode_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Months dropdown box.
        self.__months_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = "01 - January",
            size = (120, 25),
            pos = (275, 100),
            choices = ["01 - January", "02 - February", "03 - March"],
            style = wx.TE_READONLY
        )

        self.__months_dropdown_box.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        self.__months_dropdown_box.SetBackgroundColour("LIGHT GREY")

        # Years dropdown box.
        self.__years_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = "2020",
            size = (120, 25),
            pos = (275, 130),
            choices = ["2019", "2020"],
            style = wx.TE_READONLY
        )

        self.__years_dropdown_box.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        self.__years_dropdown_box.SetBackgroundColour("LIGHT GREY")
    
        # Multi-Page Handling heading label.
        self.__multi_page_handling_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Multi-Page Handling",
            size = (160, 25),
            pos = (0, 155)
        )

        self.__multi_page_handling_label.SetFont(wx.Font(
            14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Split radio button.
        self.__split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Split Documents",
            size = (120, 25),
            pos = (0, 180),
            style = wx.RB_GROUP
        )

        self.__split_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Do Not Split radio button.
        self.__do_not_split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Do Not Split Documents",
            size = (90, 25),
            pos = (160, 180)
        )

        self.__do_not_split_radio_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_middle_panel(self):
        """Creates the toolbar that runs across the middle of the GUI
        in between the top and bottom panels."""

        # Panel for middle toolbar.
        self.__middle_panel = wx.Panel(
            self.__frame,
            size = (850, 30),
            pos = (10, 265)
        )

        self.__middle_panel.SetBackgroundColour("WHITE")

        # Start button.
        self.__start_button = wx.Button(
            self.__middle_panel,
            label = "Start",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__start_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Michelin Man button.
        michelin_man_logo_path = (
            filesystem.get_resources_directory() + "images\\michelin_logo.jpg")

        michelin_man_logo = wx.Image(
            michelin_man_logo_path, wx.BITMAP_TYPE_ANY).Scale(20, 20)
        
        self.__michelin_man_button = wx.BitmapButton(
            self.__middle_panel,
            bitmap = michelin_man_logo.ConvertToBitmap(),
            size = (25, 25),
            pos = (680, 0)
        )

        # Settings button.
        self.__settings_button = wx.Button(
            self.__middle_panel,
            label = "Settings",
            size = (60, 25),
            pos = (710, 0)
        )

        self.__settings_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

        # Exit button.
        self.__exit_button = wx.Button(
            self.__middle_panel,
            label = "Exit",
            size = (60, 25),
            pos = (775, 0)
        )

        self.__exit_button.SetFont(wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_bottom_panel(self):
        """Creates the bottom panel of GUI which contains the text
        console for communicating messages and feedback to the
        user."""

        # Bottom panel.
        self.__bottom_panel = wx.Panel(
            self.__frame,
            size = (850, 230),
            pos = (0, 295)
        )

        self.__bottom_panel.SetBackgroundColour("BLUE")

