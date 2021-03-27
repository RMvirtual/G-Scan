from gui.widgets.frame import Frame
from gui.settings.panels.text_values_panel import TextValuesPanel
from gui.settings.panels.mode_options_panel import ModeOptionsPanel
from gui.settings.panels.buttons_panel import ButtonsPanel

import wx

class SettingsMenu(Frame):
    """GUI menu for viewing and amending the user's settings."""

    def __init__(self, main_application):
        """Creates a new settings menu."""

        self.__main_application = main_application
        self.__create_widgets()

    def run(self):
        """Starts the GUI application in a new thread."""
        
        self.__app.MainLoop()

    def __create_widgets(self):
        """Creates the widgects required for the gettings GUI."""

        self.__app = wx.App()
        super().__init__((895, 270), "User Settings")
        
        self.SetBackgroundColour("WHITE")
        self.__text_values_panel = TextValuesPanel(self)
        self.__mode_options_panel = ModeOptionsPanel(self)
        self.__buttons_panel = ButtonsPanel(self)

        self.Show()

    def get_user_name(self):
        """Gets the user name."""

        return self.__text_values_panel.get_user_name()

    def get_scan_directory(self):
        """Gets the scan directory text field."""

        return self.__text_values_panel.get_scan_directory()

    def get_destination_directory(self):
        """Gets the destination directory text field."""

        return self.__text_values_panel.get_destination_directory()

    def get_backup_directory(self):
        """Gets the backup directory text field."""

        return self.__text_values_panel.get_backup_directory()

    def get_paperwork_type(self):
        """Gets the value of the paperwork type dropdown box."""

        return self.__mode_options_panel.get_paperwork_type()

    def get_multi_page_handling(self):
        """Gets the value of the multi-page handling dropdown box."""

        return self.__mode_options_panel.get_multi_page_handling()

    def get_input_mode(self):
        """Gets the value of the input mode dropdown box."""

        return self.__mode_options_panel.get_input_mode()

    def get_autoprocessing_mode(self):
        """Gets the boolean status of the autoprocessing checkbox."""

        return self.__mode_options_panel.get_autoprocessing_mode()

    def set_user_name(self, user_name):
        """Sets the user name."""

        self.__text_values_panel.set_user_name(user_name)

    def set_scan_directory(self, directory):
        """Sets the scan directory text field."""

        self.__text_values_panel.set_scan_directory(directory)

    def set_destination_directory(self, directory):
        """Sets the destination directory text field."""

        self.__text_values_panel.set_destination_directory(directory)

    def set_backup_directory(self, directory):
        """Sets the backup directory text field."""

        self.__text_values_panel.set_backup_directory(directory)

    def set_paperwork_type(self, paperwork_type):
        """Sets the value of the paperwork type dropdown box."""

        self.__mode_options_panel.set_paperwork_type(paperwork_type)

    def set_multi_page_handling(self, multi_page_handling_option):
        """Sets the value of the multi-page handling dropdown box."""

        self.__mode_options_panel.set_multi_page_handling(
            multi_page_handling_option)

    def set_input_mode_dropdown_box(self, input_mode):
        """Sets the value of the input mode dropdown box."""

        self.__mode_options_panel.set_input_mode_dropdown_box(
            input_mode)

    def set_autoprocessing_checkbox(self, autoprocessing_mode):
        """Sets the boolean status of the autoprocessing checkbox."""

        self.__mode_options_panel.set_autoprocessing_checkbox(
            autoprocessing_mode)
    
    def set_save_button_function(self, callback_function):
        """Sets the save button function."""

        self.__buttons_panel.set_save_button_function(callback_function)

    def set_cancel_button_function(self, callback_function):
        """Sets the cancel button function."""

        self.__buttons_panel.set_cancel_button_function(callback_function)

    def close(self, event = None):
        """Closes the settings menu."""

        self.Close()