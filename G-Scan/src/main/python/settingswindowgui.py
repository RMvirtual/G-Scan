import wx

class SettingsWindowGUI(wx.Frame):
    """GUI Frame for viewing and amending the user's settings."""

    def __init__(self, main_application):
        """Constructor method."""
        self.__main_application = main_application
        self.__current_user = self.__main_application.get_current_user()
        self.__create_widgets()
   
    def __create_widgets(self):
        """Creates the widgets required for the settings GUI."""
        super().__init__(
            None,
            size = (895, 270),
            title = "User Settings" 
        )
        
        self.SetBackgroundColour("WHITE")
        self.__text_values_panel = TextValuesPanel(self)
        self.__mode_options_panel = ModeOptionsPanel(self)
        self.__buttons_panel = ButtonsPanel(self)
        self.Show()

class TextLabel(wx.StaticText):
    """A class representing a text label (showing a heading of data
    rather than data itself)."""

    def __init__(self, text, panel, label_position, label_size, font):
        """Constructor method."""

        super().__init__(
            panel,
            label = text,
            pos = label_position,
            size = label_size,
            style = wx.BORDER_NONE
        )

        self.SetFont(font)

class TextField(wx.StaticText):
    """A class representing a text field (showing data rather than a
    heading)."""

    def __init__(self, text, panel, field_position, field_size, font):
        """Constructor method."""

        super().__init__(
            panel,
            label = text,
            pos = field_position,
            size = field_size,
            style = wx.BORDER_SIMPLE
        )

        self.SetFont(font)
        self.SetBackgroundColour("LIGHT GREY")

class SettingsWindowPanel(wx.Panel):
    """A class representing a panel in the settings window."""

    def __init__(self, frame, panel_size, panel_position):
        """Constructor method."""

        super().__init__(
            frame,
            size = panel_size,
            pos = panel_position
        )

        self.__initialise_fonts()

    def __initialise_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = wx.Font(
            11, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        self.__body_font = wx.Font(
            14, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

    def get_body_font(self):
        """Returns the font for body text."""

        return self.__body_font

    def get_buttons_font(self):
        """Returns the font for button text."""

        return self.__button_font

class TextValuesPanel(SettingsWindowPanel):
    """A class representing the text values panel in the settings
    window GUI."""

    def __init__(self, frame):
        """Constructor method."""

        super().__init__(
            frame,
            panel_size = (860, 125),
            panel_position = (10, 10)
        )

        self.__frame = frame
        self.__create_user_name_widgets()
        self.__create_scan_directory_widgets()
        self.__create_destination_directory_widgets()
        self.__create_backup_directory_widgets()

    def __create_user_name_widgets(self):
        """Creates widgets related to the name of the current user."""

        # User Name label.
        self.__user_name_label = TextLabel(
            text = "User Name:",
            panel = self,
            label_position = (0, 0),
            label_size = (200, 20),
            font = self.get_body_font()
        )

        # User Name value label.
        self.__user_name_text_ctrl = TextField(
            text = "",
            panel = self,
            field_position = (200, 0),
            field_size = (285, 25),
            font = self.get_body_font()
        )

    def __create_scan_directory_widgets(self):
        """Creates widgets related to the current specified
        scan directory."""

        # Scan Directory label.
        self.__scan_directory_label = TextLabel(
            text = "Scan Directory:",
            panel = self,
            label_position = (0, 30),
            label_size = (200, 20),
            font = self.get_body_font()
        )

        # Scan Directory value text box.
        self.__scan_directory_value_text_box = TextField(
            text = "",
            panel = self,
            field_position = (200, 30),
            field_size = (625, 25),
            font = self.get_body_font()
        )

        # Scan Directory file dialog button.
        self.__scan_directory_file_dialog_button = wx.Button(
            self,
            label = "...",
            pos = (826, 30),
            size = (25, 25)
        )

        self.__scan_directory_file_dialog_button.SetFont(
            self.get_buttons_font())

    def __create_destination_directory_widgets(self):
        """Creates widgets related to the current specified
        destination directory."""

        # Destination Directory label.
        self.__destination_directory_label = wx.StaticText(
            self,
            label = "Destination Directory:",
            pos = (0, 60),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__destination_directory_label.SetFont(
            self.get_body_font())

        # Destination Directory value text box.
        self.__destination_directory_value_text_box = wx.StaticText(
            self,
            label = "",
            pos = (200, 60),
            size = (625, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__destination_directory_value_text_box.SetFont(
            self.get_body_font())
        
        self.__destination_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

        # Destination Directory file dialog button.
        self.__destination_directory_file_dialog_button = wx.Button(
            self,
            label = "...",
            pos = (826, 60),
            size = (25, 25)
        )

        self.__destination_directory_file_dialog_button.SetFont(
            self.get_buttons_font())

    def __create_backup_directory_widgets(self):
        """Creates widgets related to the current specified backup
        directory."""

        # Backup Directory label.
        self.__backup_directory_label = wx.StaticText(
            self,
            label = "Backup Directory:",
            pos = (0, 90),
            size = (200, 20),
            style = wx.BORDER_NONE
        )

        self.__backup_directory_label.SetFont(
            self.get_body_font())

        # Backup Directory value text box.
        self.__backup_directory_value_text_box = wx.StaticText(
            self,
            label = "",
            pos = (200, 90),
            size = (625, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__backup_directory_value_text_box.SetFont(
            self.get_body_font())
        
        self.__backup_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

        # Backup Directory file dialog button.
        self.__backup_directory_file_dialog_button = wx.Button(
            self,
            label = "...",
            pos = (826, 90),
            size = (25, 25)
        )

        self.__backup_directory_file_dialog_button.SetFont(
            self.get_buttons_font())

class ModeOptionsPanel(SettingsWindowPanel):
    """A class representing the mode options panel."""

    def __init__(self, frame):
        super().__init__(
            frame,
            panel_size = (860, 30),
            panel_position = (10, 135)
        )

        self.__frame = frame
        self.__create_paperwork_type_widgets()
        self.__create_multi_page_handling_widgets()
        self.__create_input_mode_widgets()
        self.__create_autoprocessing_widgets()

    def __create_paperwork_type_widgets(self):
        """Creates widgets related to the default paperwork type
        value."""

        # Paperwork Type label.
        self.__paperwork_type_label = TextLabel(
            text = "Default Paperwork Type:",
            panel = self,
            label_position = (0, 0),
            label_size = (200, 20),
            font = self.get_body_font()
        )

        # Paperwork Type value dropdown box.
        self.__paperwork_type_dropdown_box = wx.ComboBox(
            self,
            value = "Customer PW",
            size = (120, 25),
            pos = (200, 0),
            choices = ["Customer PW", "Loading List", "POD"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__paperwork_type_dropdown_box.SetFont(self.get_buttons_font())
        self.__paperwork_type_dropdown_box.SetBackgroundColour("LIGHT GREY")

    def __create_multi_page_handling_widgets(self):
        """Creates widgets related to the default value for
        multi-page handling."""

        # Multi-Page Handling label.
        self.__multi_page_handling_label = wx.StaticText(
            self,
            label = "Multi-Page Handling:",
            pos = (330, 0),
            size = (165, 20),
            style = wx.BORDER_NONE
        )

        self.__multi_page_handling_label.SetFont(self.get_body_font())

        # Multi-Page Handling default value dropdown box.
        self.__multi_page_handling_dropdown_box = wx.ComboBox(
            self,
            value = "Split",
            pos = (500, 0),
            size = (120, 25),
            choices = ["Do Not Split", "Split"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__multi_page_handling_dropdown_box.SetFont(self.get_buttons_font())
        self.__multi_page_handling_dropdown_box.SetBackgroundColour(
            "LIGHT GREY")

    def __create_input_mode_widgets(self):
        """Creates widgets related to the default user input mode."""

        # Input Mode label.
        self.__input_mode_label = wx.StaticText(
            self,
            label = "Input Mode:",
            pos = (630, 0),
            size = (80, 20),
            style = wx.BORDER_NONE
        )

        self.__input_mode_label.SetFont(self.get_body_font())

        # Input Mode default value dropdown box.
        self.__input_mode_dropdown_box = wx.ComboBox(
            self,
            value = "Normal",
            pos = (735, 0),
            size = (120, 25),
            choices = ["Normal", "Quick"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__input_mode_dropdown_box.SetFont(self.get_buttons_font())
        self.__input_mode_dropdown_box.SetBackgroundColour(
            "LIGHT GREY")

    def __create_autoprocessing_widgets(self):
        """Creates widgets related to the value of autoprocessing
        mode."""

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = wx.CheckBox(
            self,
            label = "POD Autoprocessing",
            size = (160, 25),
            pos = (200, 30)
        )

        self.__autoprocessing_checkbox.SetFont(wx.Font(
            9, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

class ButtonsPanel(SettingsWindowPanel):
    """A class representing the buttons panel."""

    def __init__(self, frame):
        super().__init__(
            frame,
            panel_size = (860, 30),
            panel_position = (10, 195)
        )

        self.__frame = frame
        self.__create_buttons()

    def __create_buttons(self):
        """Creates widgets for the Save and Cancel buttons."""

        # Save button.
        self.__save_button = wx.Button(
            self,
            label = "Save",
            size = (60, 25),
            pos = (200, 0))

        self.__save_button.SetFont(self.get_buttons_font())

        self.__save_button.Bind(
            wx.EVT_BUTTON,
            self.__save_button_click
        )

        # Cancel button.
        self.__cancel_button = wx.Button(
            self,
            label = "Cancel",
            size = (60, 25),
            pos = (270, 0))

        self.__cancel_button.SetFont(self.get_buttons_font())

        self.__cancel_button.Bind(
            wx.EVT_BUTTON,
            self.__cancel_button_click
        )

    def __save_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        wx.CallAfter(self.__frame.Destroy)

    def __cancel_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        wx.CallAfter(self.__frame.Destroy)
