import wx

class SettingsWindowGUI():
    """GUI for viewing and amending the user's settings."""

    def __init__(self, main_application):
        """Constructor method."""

        self.__main_application = main_application
        self.__current_user = self.__main_application.get_current_user()
        self.__create_widgets()
        
    def run(self):
        """The method to run when this object is passed
        to a thread."""
        self.__create_widgets()
    
    def __create_widgets(self):
        """Creates the widgets required for the settings GUI."""

        self.__frame = wx.Frame(
            None,
            size = (895, 270),
            title = "User Settings" 
        )

        self.__frame.SetBackgroundColour("WHITE")
        self.__set_fonts()        
        self.__create_text_values_panel()
        self.__create_mode_options_panel()
        self.__create_buttons_panel()
        self.__frame.Show()

    def __set_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        self.__body_font = wx.Font(
            14, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

    def __create_text_values_panel(self):
        """Creates the text values panel that all the text-based value related
        widgets (i.e user name and directory locations) sit within inside
        the window."""

        # Text Values panel for holding the widgets.
        self.__text_values_panel = wx.Panel(
            self.__frame,
            size = (860, 125),
            pos = (10, 10)
        )

        self.__create_user_name_widgets()
        self.__create_scan_directory_widgets()
        self.__create_destination_directory_widgets()
        self.__create_backup_directory_widgets()

    def __create_mode_options_panel(self):
        """Creates the mode options panel that all the drop-down menu
        value related widgets (i.e. paperwork type,
        multi-page handling, input mode and POD autoprocessing) sit
        withing inside the window."""

        # Mode Options panel for holding the widgets.
        self.__mode_options_panel = wx.Panel(
            self.__frame,
            size = (860, 55),
            pos = (10, 135)
        )

        self.__create_paperwork_type_widgets()
        self.__create_multi_page_handling_widgets()
        self.__create_input_mode_widgets()
        self.__create_autoprocessing_widgets()

    def __create_buttons_panel(self):
        """Creates a panel for setting the buttons."""

        self.__buttons_panel = wx.Panel(
            self.__frame,
            size = (860, 30),
            pos = (10, 195)
        )

        self.__create_buttons()

    def __create_user_name_widgets(self):
        """Creates widgets related to the name of the current user."""

        # User Name label.
        self.__user_name_label = wx.StaticText(
            self.__text_values_panel,
            label = "User Name:",
            pos = (0, 0),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__user_name_label.SetFont(self.__body_font)

        # User Name value label.
        self.__user_name_text_ctrl = wx.StaticText(
            self.__text_values_panel,
            label = self.__current_user.get_name(),
            pos = (200, 0),
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__user_name_text_ctrl.SetFont(self.__body_font)
        self.__user_name_text_ctrl.SetBackgroundColour("LIGHT GREY")

    def __create_scan_directory_widgets(self):
        """Creates widgets related to the current specified
        scan directory."""

        # Scan Directory label.
        self.__scan_directory_label = wx.StaticText(
            self.__text_values_panel,
            label = "Scan Directory:",
            pos = (0, 30),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__scan_directory_label.SetFont(self.__body_font)

        # Scan Directory value text box.
        self.__scan_directory_value_text_box = wx.StaticText(
            self.__text_values_panel,
            label = self.__current_user.get_name(),
            pos = (200, 30),
            size = (625, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__scan_directory_value_text_box.SetFont(self.__body_font)
        self.__scan_directory_value_text_box.SetBackgroundColour("LIGHT GREY")

        # Scan Directory file dialog button.
        self.__scan_directory_file_dialog_button = wx.Button(
            self.__text_values_panel,
            label = "...",
            pos = (826, 30),
            size = (25, 25)
        )

        self.__scan_directory_file_dialog_button.SetFont(
            self.__button_font)

    def __create_destination_directory_widgets(self):
        """Creates widgets related to the current specified
        destination directory."""

        # Destination Directory label.
        self.__destination_directory_label = wx.StaticText(
            self.__text_values_panel,
            label = "Destination Directory:",
            pos = (0, 60),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__destination_directory_label.SetFont(self.__body_font)

        # Destination Directory value text box.
        self.__destination_directory_value_text_box = wx.StaticText(
            self.__text_values_panel,
            label = self.__current_user.get_name(),
            pos = (200, 60),
            size = (625, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__destination_directory_value_text_box.SetFont(self.__body_font)
        self.__destination_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

        # Destination Directory file dialog button.
        self.__destination_directory_file_dialog_button = wx.Button(
            self.__text_values_panel,
            label = "...",
            pos = (826, 60),
            size = (25, 25)
        )

        self.__destination_directory_file_dialog_button.SetFont(
            self.__button_font)

    def __create_backup_directory_widgets(self):
        """Creates widgets related to the current specified backup
        directory."""

        # Backup Directory label.
        self.__backup_directory_label = wx.StaticText(
            self.__text_values_panel,
            label = "Backup Directory:",
            pos = (0, 90),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__backup_directory_label.SetFont(self.__body_font)

        # Backup Directory value text box.
        self.__backup_directory_value_text_box = wx.StaticText(
            self.__text_values_panel,
            label = self.__current_user.get_name(),
            pos = (200, 90),
            size = (625, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__backup_directory_value_text_box.SetFont(self.__body_font)
        self.__backup_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

        # Backup Directory file dialog button.
        self.__backup_directory_file_dialog_button = wx.Button(
            self.__text_values_panel,
            label = "...",
            pos = (826, 90),
            size = (25, 25)
        )

        self.__backup_directory_file_dialog_button.SetFont(
            self.__button_font)


    def __create_paperwork_type_widgets(self):
        """Creates widgets related to the default paperwork type
        value."""

        # Paperwork Type label.
        self.__paperwork_type_label = wx.StaticText(
            self.__mode_options_panel,
            label = "Default Paperwork Type:",
            pos = (0, 0),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__paperwork_type_label.SetFont(self.__body_font)

        # Paperwork Type value dropdown box.
        self.__paperwork_type_dropdown_box = wx.ComboBox(
            self.__mode_options_panel,
            value = "Customer PW",
            size = (120, 25),
            pos = (200, 0),
            choices = ["Customer PW", "Loading List", "POD"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__paperwork_type_dropdown_box.SetFont(self.__button_font)
        self.__paperwork_type_dropdown_box.SetBackgroundColour("LIGHT GREY")

    def __create_multi_page_handling_widgets(self):
        """Creates widgets related to the default value for
        multi-page handling."""

        # Multi-Page Handling label.
        self.__multi_page_handling_label = wx.StaticText(
            self.__mode_options_panel,
            label = "Multi-Page Handling:",
            pos = (330, 0),
            size = (165, 20),
            style = wx.BORDER_NONE
        )

        self.__multi_page_handling_label.SetFont(self.__body_font)

        # Multi-Page Handling default value dropdown box.
        self.__multi_page_handling_dropdown_box = wx.ComboBox(
            self.__mode_options_panel,
            value = "Split",
            pos = (500, 0),
            size = (120, 25),
            choices = ["Do Not Split", "Split"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__multi_page_handling_dropdown_box.SetFont(self.__button_font)
        self.__multi_page_handling_dropdown_box.SetBackgroundColour(
            "LIGHT GREY")

    def __create_input_mode_widgets(self):
        """Creates widgets related to the default user input mode."""

        # Input Mode label.
        self.__input_mode_label = wx.StaticText(
            self.__mode_options_panel,
            label = "Input Mode:",
            pos = (630, 0),
            size = (80, 20),
            style = wx.BORDER_NONE
        )

        self.__input_mode_label.SetFont(self.__body_font)

        # Input Mode default value dropdown box.
        self.__input_mode_dropdown_box = wx.ComboBox(
            self.__mode_options_panel,
            value = "Normal",
            pos = (735, 0),
            size = (120, 25),
            choices = ["Normal", "Quick"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__input_mode_dropdown_box.SetFont(self.__button_font)
        self.__input_mode_dropdown_box.SetBackgroundColour(
            "LIGHT GREY")

    def __create_autoprocessing_widgets(self):
        """Creates widgets related to the value of autoprocessing
        mode."""

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = wx.CheckBox(
            self.__mode_options_panel,
            label = "POD Autoprocessing",
            size = (160, 25),
            pos = (200, 30)
        )

        self.__autoprocessing_checkbox.SetFont(wx.Font(
            9, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_buttons(self):
        """Creates widgets for the Save and Cancel buttons."""

        # Save button.
        self.__save_button = wx.Button(
            self.__buttons_panel,
            label = "Save",
            size = (60, 25),
            pos = (200, 0))

        self.__save_button.SetFont(self.__button_font)

        self.__save_button.Bind(
            wx.EVT_BUTTON,
            self.__save_button_click
        )

        # Cancel button.
        self.__cancel_button = wx.Button(
            self.__buttons_panel,
            label = "Cancel",
            size = (60, 25),
            pos = (270, 0))

        self.__cancel_button.SetFont(self.__button_font)

        self.__cancel_button.Bind(
            wx.EVT_BUTTON,
            self.__cancel_button_click
        )

    def __save_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        self.__app.Destroy()

    def __cancel_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        self.__app.Destroy()