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
            size = (790, 125),
            pos = (10, 10)
        )

        self.__text_values_panel.SetBackgroundColour("YELLOW")

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
            size = (790, 100),
            pos = (10, 135)
        )

        self.__mode_options_panel.SetBackgroundColour("GREEN")

        self.__create_paperwork_type_widgets()

    def __create_buttons_panel(self):
        """Creates a panel for setting the buttons."""

        self.__buttons_panel = wx.Panel(
            self.__frame,
            size = (790, 50),
            pos = (10, 160)
        )

        self.__buttons_panel.SetBackgroundColour("RED")

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
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__scan_directory_value_text_box.SetFont(self.__body_font)
        self.__scan_directory_value_text_box.SetBackgroundColour("LIGHT GREY")

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
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__destination_directory_value_text_box.SetFont(self.__body_font)
        self.__destination_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

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
            size = (285, 25),
            style = wx.BORDER_SIMPLE
        )

        self.__backup_directory_value_text_box.SetFont(self.__body_font)
        self.__backup_directory_value_text_box.SetBackgroundColour(
            "LIGHT GREY")

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