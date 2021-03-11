import app.file_system as filesystem
import date.date as date
import wx
from gui.main_menu.panel import Panel

class TopPanel(Panel):
    """A class for the top panel of the main menu GUI."""

    def __init__(self, frame):
        """Creates a new top panel."""

        super().__init__(
            frame,
            size = (840, 255),
            position = (10, 10)
        )

        self.__create_widgets()

    def __create_widgets(self):
        """Creates the top-panel's sub-panels and underlying widgets.
        """

        self.__create_file_panel()
        self.__create_user_settings_panel()

    def __create_file_panel(self):
        """Creates the top-left panel containing the logo,
        file name and type, user input entry box, submit button,
        skip button and split document button."""

        self.__file_panel = wx.Panel(
            self,
            size = (425, 255),
            pos = (0, 0)
        )

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

        self.__file_name_label.SetFont(self.get_body_font())

        # File name value label.
        self.__file_name_text_ctrl = wx.StaticText(
            self.__file_panel,
            label = "I AM A FILE NAME",
            pos = (100, 130),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__file_name_text_ctrl.SetFont(self.get_body_font())
        self.__file_name_text_ctrl.SetBackgroundColour("LIGHT GREY")

        # File extension label.
        self.__file_extension_label = wx.StaticText(
            self.__file_panel,
            label = "File Type:",
            pos = (0, 160),
            size = (70, 20),
            style = wx.BORDER_NONE
        )

        self.__file_extension_label.SetFont(self.get_body_font())
        
        # File extension value label.
        self.__file_extension_value_label = wx.StaticText(
            self.__file_panel,
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
            self.__file_panel,
            label = "Please enter the job reference (excluding \"GR\")",
            pos = (0, 195),
            size = (285, 25),
            style = wx.BORDER_NONE
        )

        self.__input_instruction_label.SetFont(self.get_body_font())

        # User input entry box.
        self.__user_input_entry_box = wx.TextCtrl(
            self.__file_panel,
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
            self.__file_panel,
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
            self.__file_panel,
            label = "Skip",
            size = (60, 25),
            pos = (208, 225))

        self.__skip_button.SetFont(self.get_button_font())

        # Split Document button.
        self.__split_document_button = wx.Button(
            self.__file_panel,
            label = "Split Document",
            size = (120, 25),
            pos = (270, 225)
        )

        self.__split_document_button.SetFont(self.get_button_font())

    def __create_user_settings_panel(self):
        """Creates the user settings panel in the top right of the
        GUI."""

        self.__user_settings_panel = wx.Panel(
            self,
            size = (420, 255),
            pos = (425, 0)
        )

        self.__create_paperwork_type_widgets()
        self.__create_input_mode_widgets()
        self.__create_multi_page_handling_widgets()

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

        self.__paperwork_type_label.SetFont(self.get_body_font())

        # "Customer Paperwork" paperwork type radio button.
        self.__customer_paperwork_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Customer Paperwork",
            size = (160, 25),
            pos = (0, 25),
            style = wx.RB_GROUP
        )

        self.__customer_paperwork_radio_button.SetFont(self.get_button_font())

        # "Loading List" paperwork type radio button.
        self.__loading_list_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Loading List",
            size = (90, 25),
            pos = (160, 25),
        )

        self.__loading_list_radio_button.SetFont(self.get_button_font())

        # "POD" paperwork type radio button.
        self.__pod_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "POD",
            size = (45, 25),
            pos = (265, 25)
        )

        self.__pod_radio_button.SetFont(self.get_button_font())

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

        self.__input_mode_label.SetFont(self.get_body_font())

        # Normal Mode radio button.
        self.__normal_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Normal Mode",
            size = (120, 25),
            pos = (0, 110),
            style = wx.RB_GROUP
        )

        self.__normal_mode_radio_button.SetFont(self.get_button_font())

        # Quick Mode radio button.
        self.__quick_mode_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Quick Mode",
            size = (90, 25),
            pos = (160, 110),
        )

        self.__quick_mode_radio_button.SetFont(self.get_button_font())

        # Months dropdown box.
        month_options = date.get_months_as_strings()
        current_month = date.get_current_month().get_full_code()

        self.__months_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = current_month,
            size = (120, 25),
            pos = (275, 110),
            choices = month_options,
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__months_dropdown_box.SetFont(self.get_button_font())
        self.__months_dropdown_box.SetBackgroundColour("LIGHT GREY")

        # Years dropdown box.
        year_options = date.get_years_as_strings()
        current_year = date.get_current_year().get_full_code()

        self.__years_dropdown_box = wx.ComboBox(
            self.__user_settings_panel,
            value = current_year,
            size = (120, 25),
            pos = (275, 140),
            choices = year_options,
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__years_dropdown_box.SetFont(self.get_button_font())
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

        self.__multi_page_handling_label.SetFont(self.get_body_font())

        # Split radio button.
        self.__split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Split Documents",
            size = (120, 25),
            pos = (0, 200),
            style = wx.RB_GROUP
        )

        self.__split_radio_button.SetFont(self.get_button_font())

        # Do Not Split radio button.
        self.__do_not_split_radio_button = wx.RadioButton(
            self.__user_settings_panel,
            label = "Do Not Split Documents",
            size = (90, 25),
            pos = (160, 200)
        )

        self.__do_not_split_radio_button.SetFont(self.get_button_font())

    def __submit_button_click(self, event = None):
        """Defines the behaviour to follow when the submit button
        is clicked, activating the main application's submit
        workflow method."""

        print("Hello")
