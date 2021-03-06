import wx
from app import filesystem
import threading

class GUI():
    """GUI for running the main application."""

    def __init__(self, main_application, gui_semaphore):
        """Constructor method."""

        self.__main_application = main_application
        self.__gui_semaphore = gui_semaphore
        
    def run(self):
        """Starts the GUI application."""

        self.__gui_semaphore.acquire()

        self.__app = wx.App(False)
        self.__set_fonts()
        self.__create_widgets()

        self.__gui_semaphore.release()

        self.__app.MainLoop()

    def __create_widgets(self):
        """Creates the widgets required for the GUI."""

        self.__frame = wx.Frame(
            None,
            size = (870, 575),
            title = "G-Scan"
        )

        self.__frame.SetBackgroundColour("WHITE")
        self.__create_panels()

        self.__frame.Show()

    def __set_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = self.__create_font(11)
        self.__body_font = self.__create_font(14)

    def __create_font(self, font_size):
        """Creates a calibri font to be used."""

        font = wx.Font(
            font_size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        return font

    def __create_panels(self):
        """Creates the main panels for widgets to be instantiated in.
        For use with the __create_widgets() method."""

        self.__create_top_panel()
        self.__create_middle_panel()
        self.__create_bottom_panel()

    def __create_top_panel(self):
        """Creates the top panel's sub-panels and corresponding
        widgets."""

        self.__top_panel = wx.Panel(
            self.__frame,
            size = (840, 255),
            pos = (10, 10)
        )

        self.__create_file_panel()
        self.__create_user_settings_panel()

    def __create_middle_panel(self):
        """Creates the middle panel that contains the toolbar that runs
        across the middle of the GUI in between the top and bottom
        panels."""

        self.__middle_panel = wx.Panel(
            self.__frame,
            size = (850, 30),
            pos = (10, 265)
        )

        self.__create_toolbar_widgets()

    def __create_bottom_panel(self):
        """Creates the bottom panel of GUI which contains the text
        console for communicating messages and feedback to the
        user."""

        # Bottom panel.
        self.__bottom_panel = wx.Panel(
            self.__frame,
            size = (840, 230),
            pos = (10, 295)
        )

        # Text console display.
        self.__text_console_output_box = wx.TextCtrl(
            self.__bottom_panel,
            size = (835, 230),
            pos = (0, 0),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE
        )

        self.__text_console_output_box.SetBackgroundColour("LIGHT GREY")

    def __create_file_panel(self):
        """Creates the top-left panel containing the logo,
        file name and type, user input entry box, submit button,
        skip button and split document button."""

        self.__file_panel = wx.Panel(
            self.__top_panel,
            size = (425, 255),
            pos = (0, 0)
        )

        self.__create_logo_widget()
        self.__create_file_detail_widgets()
        self.__create_user_input_widgets()

    def __create_user_settings_panel(self):
        """Creates the user settings panel in the top right of the
        GUI."""

        self.__user_settings_panel = wx.Panel(
            self.__top_panel,
            size = (420, 255),
            pos = (425, 0)
        )

        self.__create_paperwork_type_widgets()
        self.__create_input_mode_widgets()
        self.__create_multi_page_handling_widgets()

    def __create_toolbar_widgets(self):
        """Creates widgets related to the middle toolbar."""

        # Start button.
        self.__start_button = wx.Button(
            self.__middle_panel,
            label = "Start",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__start_button.SetFont(self.__button_font)

        self.__start_button.Bind(
            wx.EVT_BUTTON,
            self.__start_button_click
        )

        # Quick Mode user aid message for displaying a preview of the
        # output that quick mode will calculate based on the current
        # user settings and what they have entered so far in the user
        # input entry box.
        self.__quick_mode_preview_text = wx.StaticText(
            self.__middle_panel,
            label = "",
            size = (180, 14),
            pos = (155, 3),
            style = wx.ALIGN_RIGHT
        )

        self.__quick_mode_preview_text.SetFont(wx.Font(
            12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

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

        self.__settings_button.SetFont(self.__button_font)

        self.__settings_button.Bind(
            wx.EVT_BUTTON,
            self.__settings_button_click
        )

        # Exit button.
        self.__exit_button = wx.Button(
            self.__middle_panel,
            label = "Exit",
            size = (60, 25),
            pos = (775, 0)
        )

        self.__exit_button.SetFont(self.__button_font)

        self.__exit_button.Bind(
            wx.EVT_BUTTON,
            self.__exit_button_click
        )

    def __create_logo_widget(self):
        """Creates the logo in the file panel."""

        gscan_logo_path = (
            filesystem.get_resources_directory() + "images\\g-scan_logo.png")

        logo_image_bitmap = wx.Bitmap(wx.Image(
            gscan_logo_path, wx.BITMAP_TYPE_ANY))
        
        self.__logo_image = wx.StaticBitmap(
            self.__file_panel,
            wx.ID_ANY,
            logo_image_bitmap
        )

    def __create_file_detail_widgets(self):
        """Creates widgets related to displaying details about the
        current file being processed."""

        # File name label.
        self.__file_name_label = wx.StaticText(
            self.__file_panel,
            label = "File Name:",
            pos = (0, 130),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_name_label.SetFont(self.__body_font)

        # File name value label.
        self.__file_name_text_ctrl = wx.StaticText(
            self.__file_panel,
            label = "I AM A FILE NAME",
            pos = (100, 130),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_name_text_ctrl.SetFont(self.__body_font)
        self.__file_name_text_ctrl.SetBackgroundColour("LIGHT GREY")

        # File extension label.
        self.__file_extension_label = wx.StaticText(
            self.__file_panel,
            label = "File Type:",
            pos = (0, 160),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_extension_label.SetFont(self.__body_font)
        
        # File extension value label.
        self.__file_extension_value_label = wx.StaticText(
            self.__file_panel,
            label = ".ext",
            pos = (100, 160),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_extension_value_label.SetFont(self.__body_font)
        self.__file_extension_value_label.SetBackgroundColour("LIGHT GREY")

    def __create_user_input_widgets(self):
        """Creates widgets related to user input."""

        # Input instruction label.
        self.__input_instruction_label = wx.StaticText(
            self.__file_panel,
            label = "Please enter the job reference (excluding \"GR\")",
            pos = (0, 195),
            size = (285, 25),
            style = wx.BORDER_NONE
        )

        self.__input_instruction_label.SetFont(self.__body_font)

        # User input entry box.
        self.__user_input_entry_box = wx.TextCtrl(
            self.__file_panel,
            value = wx.EmptyString,
            pos = (0, 225),
            size = (140, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__user_input_entry_box.SetFont(self.__body_font)
        self.__user_input_entry_box.SetBackgroundColour("LIGHT GREY")
        self.__user_input_entry_box.SetMaxLength(11)

        # Submit button.
        self.__submit_button = wx.Button(
            self.__file_panel,
            label = "Submit",
            size = (60, 25),
            pos = (140, 225))

        self.__submit_button.SetFont(self.__button_font)

        self.__submit_button.Bind(
            wx.EVT_BUTTON,
            self.__submit_button_click,
            self.__submit_button
        )

        # Skip button.
        self.__skip_button = wx.Button(
            self.__file_panel,
            label = "Skip",
            size = (60, 25),
            pos = (208, 225))

        self.__skip_button.SetFont(self.__button_font)

        # Split Document button.
        self.__split_document_button = wx.Button(
            self.__file_panel,
            label = "Split Document",
            size = (120, 25),
            pos = (270, 225)
        )

        self.__split_document_button.SetFont(self.__button_font)

    def __create_paperwork_type_widgets(self):
        """Creates the widgets related to the paperwork type settings
        in the GUI."""

        # Paperwork type heading label.
        self.__paperwork_type_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Paperwork Type",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__paperwork_type_label.SetFont(self.__body_font)

        # "Customer Paperwork" paperwork type radio button.
        self.__customer_paperwork_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Customer Paperwork",
            size = (160, 25),
            pos = (0, 25),
            style = wx.RB_GROUP
        )

        self.__customer_paperwork_radio_button.SetFont(self.__button_font)

        # "Loading List" paperwork type radio button.
        self.__loading_list_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Loading List",
            size = (90, 25),
            pos = (160, 25),
        )

        self.__loading_list_radio_button.SetFont(self.__button_font)

        # "POD" paperwork type radio button.
        self.__pod_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "POD",
            size = (45, 25),
            pos = (265, 25)
        )

        self.__pod_radio_button.SetFont(self.__button_font)

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = wx.CheckBox(
            self.__user_settings_panel,
            label = "Autoprocess",
            size = (85, 25),
            pos = (320, 25)
        )

        self.__autoprocessing_checkbox.SetFont(wx.Font(
            9, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_input_mode_widgets(self):
        """Creates the widgets for setting the input mode in the
        GUI."""

        # Input Mode heading label.
        self.__input_mode_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Input Mode",
            size = (60, 25),
            pos = (0, 85)
        )

        self.__input_mode_label.SetFont(self.__body_font)

        # Normal Mode radio button.
        self.__normal_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Normal Mode",
            size = (120, 25),
            pos = (0, 110),
            style = wx.RB_GROUP
        )

        self.__normal_mode_radio_button.SetFont(self.__button_font)

        # Quick Mode radio button.
        self.__quick_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Quick Mode",
            size = (90, 25),
            pos = (160, 110),
        )

        self.__quick_mode_radio_button.SetFont(self.__button_font)

        # Months dropdown box.
        self.__months_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = "01 - January",
            size = (120, 25),
            pos = (275, 110),
            choices = ["01 - January", "02 - February", "03 - March"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__months_dropdown_box.SetFont(self.__button_font)
        self.__months_dropdown_box.SetBackgroundColour("LIGHT GREY")

        # Years dropdown box.
        self.__years_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = "2020",
            size = (120, 25),
            pos = (275, 140),
            choices = ["2019", "2020"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__years_dropdown_box.SetFont(self.__button_font)
        self.__years_dropdown_box.SetBackgroundColour("LIGHT GREY")

    def __create_multi_page_handling_widgets(self):
        """Creates the widgets responsible for setting multi-page
        handling's behaviour in the program."""

        # Multi-Page Handling heading label.
        self.__multi_page_handling_label = wx.StaticText(
            self.__user_settings_panel,
            label = "Multi-Page Handling",
            size = (160, 25),
            pos = (0, 175)
        )

        self.__multi_page_handling_label.SetFont(self.__body_font)

        # Split radio button.
        self.__split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Split Documents",
            size = (120, 25),
            pos = (0, 200),
            style = wx.RB_GROUP
        )

        self.__split_radio_button.SetFont(self.__button_font)

        # Do Not Split radio button.
        self.__do_not_split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Do Not Split Documents",
            size = (90, 25),
            pos = (160, 200)
        )

        self.__do_not_split_radio_button.SetFont(self.__button_font)

    def __submit_button_click(self, event = None):
        """Defines the behaviour to follow when the submit button
        is clicked, activating the main application's submit
        workflow method."""

        print("Hello")
    
    def __start_button_click(self, event = None):
        """Defines the behavior to follow when the start button
        is clicked on, activating the main application's start
        workflow method."""

        self.__main_application.start()

    def __exit_button_click(self, event = None):
        """Defines the behaviour to follow when the exit button
        is clicked on, activating the main application's exit
        workflow method."""

        self.__main_application.exit()

    def __settings_button_click(self, event = None):
        """Defines the behaviour to follow when the exit button
        is clicked on, activating the main application's exit
        workflow method."""
        
        print("Settings button clicked.")
        self.__main_application.open_settings_menu()

    def get_current_paperwork_type(self):
        """Gets the value of the paperwork type variable based on
        which button has been selected."""

        return "POD"
    
    def get_user_input(self):
        """Gets the value of the user's input."""

        return "GR191000000"

    def get_current_input_mode(self):
        """Gets the current input mode setting (i.e. Normal or
        Quick)."""

        return "Normal"
    
    def get_autoprocessing_mode(self):
        """Gets the current autoprocessing mode setting (True or
        False)"""

        return True
    
    def clear_user_input(self):
        """Clears the user's input from the user input text entry
        box."""

        return True
    
    def get_multi_page_handling_mode(self):
        """Returns the current setting of multi-page handling."""

        return "Split"

    def write_log(self, text):
        """Writes a string of text to the console output log."""

        self.__text_console_output_box.write(text)

    def set_quick_mode_hint_text(self, text):
        """Overwrites the text found in the quick mode hint text
        box."""
        
        self.__quick_mode_preview_text.SetLabel(text)
