from gui.widgets.frame import Frame
from gui.mainmenu.panels.bottompanel.bottom_panel import BottomPanel
from gui.mainmenu.panels.middlepanel.middle_panel import MiddlePanel
from gui.mainmenu.panels.toppanel.top_panel import TopPanel

import wx

class MainMenu(Frame):
    """GUI for running the main application."""

    def __init__(self, main_application):
        """Constructor method."""

        self.__main_application = main_application
        self.__application_lock = main_application.get_lock()

    def run(self):
        """Starts the GUI application."""
        
        with self.__application_lock:
            self.__app = wx.App(False)

            super().__init__((870, 575), "G-Scan")
            self.__create_widgets()
       
        self.__app.MainLoop()

    def __create_widgets(self):
        """Creates the widgets required for the GUI."""

        self.__create_panels()
        self.Show()

    def __create_panels(self):
        """Creates the main panels for widgets to be instantiated in.
        For use with the __create_widgets() method.
        """

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

    def get_main_application(self):
        """Gets the main application responsible for running the main
        menu.
        """

        return self.__main_application

    def set_submit_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the submit button is
        clicked.
        """

        self.__top_panel.set_submit_button_function(callback_function)

    def set_skip_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the skip button is
        clicked.
        """

        self.__top_panel.set_skip_button_function(callback_function)

    def set_split_document_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the split document button
        is clicked.
        """

        self.__top_panel.set_split_document_button_function(callback_function)