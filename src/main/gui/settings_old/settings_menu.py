from src.main.gui.widgets.frame import Frame
from src.main.gui.settings_old.panels.text_values_panel import TextValuesPanel
from src.main.gui.settings_old.panels.mode_options_panel import ModeOptionsPanel
from src.main.gui.settings_old.panels.buttons_panel import ButtonsPanel


class SettingsMenu(Frame):
    def __init__(self):
        self.__create_widgets()

    def __create_widgets(self):
        super().__init__((895, 270), "User Settings")
        
        self.SetBackgroundColour("WHITE")
        self.__text_values_panel = TextValuesPanel(self)
        self.__mode_options_panel = ModeOptionsPanel(self)
        self.__buttons_panel = ButtonsPanel(self)

        self.Show()

    def get_user_name(self):
        return self.__text_values_panel.get_user_name()

    def get_scan_directory(self):
        return self.__text_values_panel.get_scan_directory()

    def get_destination_directory(self):
        return self.__text_values_panel.get_destination_directory()

    def get_backup_directory(self):
        return self.__text_values_panel.get_backup_directory()

    def get_paperwork_type(self):
        return self.__mode_options_panel.get_paperwork_type()

    def get_multi_page_handling(self):
        return self.__mode_options_panel.get_multi_page_handling()

    def get_input_mode(self):
        return self.__mode_options_panel.get_input_mode()

    def get_autoprocessing_mode(self):
        return self.__mode_options_panel.get_autoprocessing_mode()

    def set_user_name(self, user_name):
        self.__text_values_panel.set_user_name(user_name)

    def set_scan_directory(self, directory: str):
        if directory:
            self.__text_values_panel.set_scan_directory(directory)

    def set_destination_directory(self, directory):
        if directory:
            self.__text_values_panel.set_destination_directory(directory)

    def set_backup_directory(self, directory):
        if directory:
            self.__text_values_panel.set_backup_directory(directory)

    def set_paperwork_type(self, paperwork_type):
        self.__mode_options_panel.set_paperwork_type(paperwork_type)

    def set_multi_page_handling(self, multi_page_handling_option):
        self.__mode_options_panel.set_multi_page_handling(
            multi_page_handling_option)

    def set_input_mode_dropdown_box(self, input_mode):
        self.__mode_options_panel.set_input_mode_dropdown_box(
            input_mode)

    def set_autoprocessing_checkbox(self, autoprocessing_mode):
        self.__mode_options_panel.set_autoprocessing_checkbox(
            autoprocessing_mode)
    
    def set_save_button_function(self, callback_function):
        self.__buttons_panel.set_save_button_function(callback_function)

    def set_cancel_button_function(self, callback_function):
        self.__buttons_panel.set_cancel_button_function(callback_function)

    def set_browse_backup_directory_button_function(self, callback_function):
        self.__text_values_panel.set_browse_backup_directory_button_function(
            callback_function)

    def set_browse_scan_directory_button_function(self, callback_function):
        self.__text_values_panel.set_browse_scan_directory_button_function(
            callback_function)

    def set_browse_destination_directory_button_function(
            self, callback_function):
        sub_panel = self.__text_values_panel

        sub_panel.set_browse_destination_directory_button_function(
            callback_function)

    def close(self, event=None):
        self.Close()