import wx
from app import file_system
import date.date
from gui.main_menu.top_panel import TopPanel
import threading

class MainMenu(wx.Frame):
    """GUI for running the main application."""

    def __init__(self, main_application, application_semaphore):
        """Constructor method."""

        self.__main_application = main_application
        self.__application_semaphore = application_semaphore
        
    def run(self):
        """Starts the GUI application."""

        self.__application_semaphore.acquire()

        self.__app = wx.App(False)
        self.__set_fonts()
        self.__create_widgets()

        self.__application_semaphore.release()

        self.__app.MainLoop()

    def __create_widgets(self):
        """Creates the widgets required for the GUI."""

        super().__init__(
            None,
            size = (870, 575),
            title = "G-Scan"
        )

        self.SetBackgroundColour("WHITE")
        self.__create_panels()

        self.Show()

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

        self.__top_panel = TopPanel(self)

    def __create_middle_panel(self):
        """Creates the middle panel that contains the toolbar that runs
        across the middle of the GUI in between the top and bottom
        panels."""

        self.__middle_panel = wx.Panel(
            self,
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
            self,
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
            file_system.get_resources_directory() + "images\\michelin_logo.jpg")

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