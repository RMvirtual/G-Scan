import wx
from app import file_system
import date.date
from gui.mainmenu.panels.bottompanel.bottom_panel import BottomPanel
from gui.mainmenu.panels.middlepanel.middle_panel import MiddlePanel
from gui.mainmenu.panels.toppanel.top_panel import TopPanel
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

        self.__top_panel = TopPanel(self)
        self.__middle_panel = MiddlePanel(self)
        self.__bottom_panel = BottomPanel(self)
    
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

        self.__bottom_panel.write_log(text)

    def set_quick_mode_hint_text(self, text):
        """Overwrites the text found in the quick mode hint text
        box."""
        
        self.__middle_panel.set_quick_mode_hint_text(text)
