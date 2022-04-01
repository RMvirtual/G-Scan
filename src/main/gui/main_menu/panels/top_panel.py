from src.main.gui.widgets.panel import Panel
from src.main.gui.main_menu.panels.subpanels.file_panel import FilePanel
from src.main.gui.main_menu.panels.subpanels.user_settings_panel import (
    UserSettingsPanel)


class TopPanel(Panel):
    """A class for the top panel of the main menu GUI."""

    def __init__(self, frame):
        """Creates a new top panel."""

        super().__init__(frame, (840, 255), (10, 10))
        self.__create_widgets()

    def __create_widgets(self):
        """Creates the top-panel's sub-panels and underlying 
        widgets.
        """

        self.__file_panel = FilePanel(self)
        self.__user_settings_panel = UserSettingsPanel(self)

    def set_submit_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the submit button is
        clicked.
        """

        self.__file_panel.set_submit_button_function(callback_function)

    def set_skip_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the skip button is
        clicked.
        """

        self.__file_panel.set_skip_button_function(callback_function)

    def set_split_document_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the split document button
        is clicked.
        """

        self.__file_panel.set_split_document_button_function(
            callback_function)

    def get_paperwork_type(self):
        """Gets the current selection for paperwork type."""

        return self.__user_settings_panel.get_paperwork_type()

    def get_input_mode(self):
        """Gets the current selection for input mode."""

        return self.__user_settings_panel.get_input_mode()

    def get_multi_page_handling(self):
        """Gets the current selection for multi-page handling."""

        return self.__user_settings_panel.get_multi_page_handling()

    def get_autoprocessing_mode(self):
        """Gets the current value for the autoprocessing mode."""

        return self.__user_settings_panel.get_autoprocessing_mode()

    def set_paperwork_type(self, paperwork_type: str):
        self.__user_settings_panel.set_paperwork_type(paperwork_type)

    def set_multi_page_handling(self, multi_page_handling: str):
        self.__user_settings_panel.set_multi_page_handling(
            multi_page_handling)

    def set_input_mode(self, input_mode: str):
        self.__user_settings_panel.set_input_mode(input_mode)

    def set_autoprocessing_mode(self, autoprocessing: bool):
        self.__user_settings_panel.set_autoprocessing_mode(autoprocessing)

    def get_months_dropdown_box_value(self) -> str:
        """Gets the month dropdown box value."""

        return self.__user_settings_panel.get_months_dropdown_box_value()

    def get_years_dropdown_box_value(self) -> str:
        """Gets the year dropdown box value."""

        return self.__user_settings_panel.get_years_dropdown_box_value()

    def bind_event_handler_to_user_input_box(self, event_handler) -> None:
        self.__file_panel.bind_event_handler_to_user_input_box(event_handler)

