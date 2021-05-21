from gui.widgets.frame import Frame
from gui.mainmenu.panels.top_panel import TopPanel
from gui.mainmenu.panels.middle_panel import MiddlePanel
from gui.mainmenu.panels.bottom_panel import BottomPanel

class MainMenu(Frame):
    """GUI for running the main application."""

    def __init__(self):
        """Constructor method."""

        self.__create_widgets()

    def close(self):
        """Closes the app."""

        self.Close()

    def __create_widgets(self):
        """Creates the widgets required for the GUI."""
       
        super().__init__((870, 575), "G-Scan")
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

    def set_exit_button_function(self, callback_function):
        """Sets the function to be run when the exit button is
        clicked."""

        self.__middle_panel.set_exit_button_function(callback_function)

    def set_start_button_function(self, callback_function):
        """Sets the function to be run when the exit button is
        clicked."""

        self.__middle_panel.set_start_button_function(callback_function)

    def set_settings_button_function(self, callback_function):
        """Sets the function to be run when the settings button is
        clicked."""

        self.__middle_panel.set_settings_button_function(callback_function)

    def set_michelin_man_button_function(self, callback_function):
        """Sets the function to be run when the michelin man button is
        clicked."""

        self.__middle_panel.set_michelin_man_button_function(callback_function)

    def get_paperwork_type(self):
        """Gets the current selection for paperwork type."""

        return self.__top_panel.get_paperwork_type()

    def get_input_mode(self):
        """Gets the current selection for input mode."""

        return self.__top_panel.get_input_mode()

    def get_multi_page_handling(self):
        """Gets the current selection for multi-page handling."""

        return self.__top_panel.get_multi_page_handling()

    def get_autoprocessing_mode(self):
        return self.__top_panel.get_autoprocessing_mode()

    def set_paperwork_type(self, paperwork_type: str):
        self.__top_panel.set_paperwork_type(paperwork_type)

    def set_multi_page_handling(self, multi_page_handling: str):
        self.__top_panel.set_multi_page_handling(multi_page_handling)

    def set_input_mode(self, input_mode: str):
        self.__top_panel.set_input_mode(input_mode)

    def set_autoprocessing_mode(self, autoprocessing: bool):
        self.__top_panel.set_autoprocessing_mode(autoprocessing)

    def get_months_dropdown_box_value(self) -> str:
        """Gets the month dropdown box value."""

        return self.__top_panel.get_months_dropdown_box_value()

    def get_years_dropdown_box_value(self) -> str:
        """Gets the year dropdown box value."""

        return self.__top_panel.get_years_dropdown_box_value()

    def bind_event_handler_to_user_input_box(self, event_handler) -> None:
        self.__top_panel.bind_event_handler_to_user_input_box(event_handler)