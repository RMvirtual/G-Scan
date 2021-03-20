import date.date as date

from gui.widgets.checkboxes import CheckBox
from gui.widgets.dropdownboxes import DropdownBox
from gui.widgets.panel import Panel
from gui.widgets.radio_buttons import RadioButtonMaster, RadioButtonSubject
from gui.widgets.text import TextLabel

class UserSettingsPanel(Panel):
    """A class modelling the user settings panel window found in the
    top panel of the main menu GUI.
    """

    def __init__(self, top_panel):
        """Creates a new user settings panel widget."""

        super().__init__(
            top_panel,
            size = (420, 255),
            position = (425, 0)
        )

        self.__create_widgets()

    def __create_widgets(self):
        """Creates the widgets required for the user settings panel."""

        self.__create_paperwork_type_widgets()
        self.__create_input_mode_widgets()
        self.__create_multi_page_handling_widgets()

    def __create_paperwork_type_widgets(self):
        """Creates the widgets related to the paperwork type settings
        in the GUI."""

        self.__paperwork_type_heading = TextLabel(
            self, "Paperwork Type", (60, 25), (0, 0))

        self.__customer_paperwork_radio_button = RadioButtonMaster(
            self, "Customer Paperwork", (160, 25), (0, 25))

        self.__loading_list_radio_button = RadioButtonSubject(
            self, "Loading List", (90, 25), (160, 25))

        self.__pod_radio_button = RadioButtonSubject(
            self, "POD", (45, 25), (265, 25))

        self.__autoprocessing_checkbox = CheckBox(
            self, "Autoprocess", (85, 25), (320, 25))

    def __create_input_mode_widgets(self):
        """Creates the widgets for setting the input mode in the
        GUI."""

        self.__input_mode_label = TextLabel(
            self, "Input Mode", (60, 25), (0, 85))

        self.__normal_mode_radio_button = RadioButtonMaster(
            self, "Normal Mode", (120, 25), (0, 110))

        self.__quick_mode_radio_button = RadioButtonSubject(
            self, "Quick Mode", (90, 25), (160, 110))

        month_options = date.get_months_as_strings()
        current_month = date.get_current_month().get_full_code()

        self.__months_dropdown_box = DropdownBox(
            self, current_month, (120, 25), (275, 110), month_options)

        year_options = date.get_years_as_strings()
        current_year = date.get_current_year().get_full_code()

        self.__years_dropdown_box = DropdownBox(
            self, current_year, (120, 25), (275, 140), year_options)

    def __create_multi_page_handling_widgets(self):
        """Creates the widgets responsible for setting multi-page
        handling's behaviour in the program."""

        self.__multi_page_handling_label = TextLabel(
            self, "Multi-Page Handling", (160, 25), (0, 175))

        self.__split_radio_button = RadioButtonMaster(
            self, "Split Documents", (120, 25), (0, 200))

        self.__do_not_split_radio_button = RadioButtonSubject(
            self, "Do Not Split Documents", (90, 25), (160, 200))
