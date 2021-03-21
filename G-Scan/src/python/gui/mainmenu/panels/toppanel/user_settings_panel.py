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

        self.__create_paperwork_type_heading()
        self.__create_paperwork_type_radio_buttons()
        self.__create_autoprocessing_checkbox()

    def __create_paperwork_type_heading(self):
        """Creates the paperwork type heading."""

        attributes = self.__create_paperwork_type_heading_attributes()
        self.__paperwork_type_heading = TextLabel.from_attributes(attributes)

    def __create_paperwork_type_heading_attributes(self):
        """Creates the attributes required to instantiate the paperwork
        type heading.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Paperwork Type"
        attributes.size = (60, 25)
        attributes.position = (0, 0)

        return attributes

    def __create_paperwork_type_radio_buttons(self):
        """Creates the paperwork type radio buttons."""

        self.__create_customer_paperwork_radio_button()
        self.__create_loading_list_radio_button()
        self.__create_pod_radio_button()
 
    def __create_customer_paperwork_radio_button(self):
        """Creates the customer paperwork radio button."""

        attributes = (
            self.__create_customer_paperwork_radio_button_attributes())

        self.__customer_paperwork_radio_button = (
            RadioButtonMaster.from_attributes(attributes))

    def __create_customer_paperwork_radio_button_attributes(self):
        """Creates the attributes required to create the customer
        paperwork radio button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Customer Paperwork"
        attributes.size = (160, 25)
        attributes.position = (0, 25)

        return attributes

    def __create_loading_list_radio_button(self):
        """Creates the loading list radio button."""

        attributes = (
            self.__create_loading_list_radio_button_attributes())

        self.__loading_list_radio_button = (
            RadioButtonSubject.from_attributes(attributes))

    def __create_loading_list_radio_button_attributes(self):
        """Creates the attributes required to create the POD radio
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Loading List"
        attributes.size = (90, 25)
        attributes.position = (160, 25)

        return attributes

    def __create_pod_radio_button(self):
        """Creates the customer paperwork radio button."""

        attributes = (
            self.__create_pod_radio_button_attributes())

        self.__pod_radio_button = (
            RadioButtonSubject.from_attributes(attributes))

    def __create_pod_radio_button_attributes(self):
        """Creates the attributes required to create the POD radio
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "POD"
        attributes.size = (45, 25)
        attributes.position = (265, 25)

        return attributes

    def __create_autoprocessing_checkbox(self):
        """Creates the autoprocessing checkbox."""

        attributes = self.__create_autoprocessing_checkbox_attributes()
        self.__autoprocessing_checkbox = CheckBox.from_attributes(attributes)

    def __create_autoprocessing_checkbox_attributes(self):
        """Creates the attributes required to create the autoprocessing
        checkbox.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Autoprocess"
        attributes.size = (85, 25)
        attributes.position = (320, 25)

        return attributes

    def __create_input_mode_widgets(self):
        """Creates the widgets for setting the input mode in the
        GUI."""

        self.__input_mode_label = TextLabel(
            self, "Input Mode", (60, 25), (0, 85))

        self.__create_input_mode_radio_buttons()
        self.__create_month_options_dropdown_box()
        self.__create_year_options_dropdown_box()

    def __create_input_mode_radio_buttons(self):
        """Creates the input mode radio buttons."""

        self.__normal_mode_radio_button = RadioButtonMaster(
            self, "Normal Mode", (120, 25), (0, 110))

        self.__quick_mode_radio_button = RadioButtonSubject(
            self, "Quick Mode", (90, 25), (160, 110))

    def __create_month_options_dropdown_box(self):
        """Creates the month options dropdown box for quick mode."""

        month_options = date.get_months_as_strings()
        current_month = date.get_current_month().get_full_code()

        self.__months_dropdown_box = DropdownBox(
            self, current_month, (120, 25), (275, 110), month_options)

    def __create_year_options_dropdown_box(self):
        """Creates the year options dropdown box for quick mode."""

        year_options = date.get_years_as_strings()
        current_year = date.get_current_year().get_full_code()

        self.__years_dropdown_box = DropdownBox(
            self, current_year, (120, 25), (275, 140), year_options)

    def __create_multi_page_handling_widgets(self):
        """Creates the widgets responsible for setting multi-page
        handling's behaviour in the program."""

        self.__multi_page_handling_label = TextLabel(
            self, "Multi-Page Handling", (160, 25), (0, 175))

        self.__create_multi_page_handling_radio_buttons()

    def __create_multi_page_handling_radio_buttons(self):
        """Creates the multi-page handling radio buttons responsible
        for determining whether to split multi-page PDF files."""

        self.__split_radio_button = RadioButtonMaster(
            self, "Split Documents", (120, 25), (0, 200))

        self.__do_not_split_radio_button = RadioButtonSubject(
            self, "Do Not Split Documents", (90, 25), (160, 200))
