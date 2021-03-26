import wx

from gui.widgets.panel import Panel
from gui.widgets.text import TextLabel
from gui.widgets.dropdownboxes import DropdownBox
from gui.widgets.checkboxes import CheckBox

class ModeOptionsPanel(Panel):
    """A class representing the mode options panel."""

    def __init__(self, frame):
        super().__init__(frame, (860, 30), (10, 135))

        self.__create_paperwork_type_widgets()
        self.__create_multi_page_handling_widgets()
        self.__create_input_mode_widgets()
        self.__create_autoprocessing_widgets()

    def __create_paperwork_type_widgets(self):
        """Creates widgets related to the default paperwork type
        value."""

        # Paperwork Type label.
        self.__paperwork_type_label = TextLabel(
            self, "Default Paperwork Type:", (200, 20), (0, 0))

        # Paperwork Type value dropdown box.
        self.__paperwork_type_dropdown_box = DropdownBox(
            self, "lol", (120, 25), (200, 0),
            ["Customer PW", "Loading List", "POD"]
        )

    def __create_multi_page_handling_widgets(self):
        """Creates widgets related to the default value for
        multi-page handling."""

        # Multi-Page Handling label.
        self.__multi_page_handling_label = TextLabel(
            self, "Multi-Page Handling:", (165, 20), (330, 0))

        # Multi-Page Handling default value dropdown box.
        self.__multi_page_handling_dropdown_box = DropdownBox(
            self, "lol", (120, 25), (500, 0),
            options = ["Do Not Split", "Split"]
        )

    def __create_input_mode_widgets(self):
        """Creates widgets related to the default user input mode."""

        # Input Mode label.
        self.__input_mode_label = TextLabel(
            self, "Input Mode:", (80, 20), (630, 0))

        # Input Mode default value dropdown box.
        self.__input_mode_dropdown_box = DropdownBox(
            self, "lol", (120, 25), (735, 0),
            options = ["Normal", "Quick"]
        )

    def __create_autoprocessing_widgets(self):
        """Creates widgets related to the value of autoprocessing
        mode."""

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = CheckBox(
            self, "POD Autoprocessing", (160, 25), (200, 30))

    def get_paperwork_type(self):
        """Gets the value of the paperwork type dropdown box."""

        self.__paperwork_type_dropdown_box.GetValue()

    def get_multi_page_handling(self):
        """Gets the value of the multi-page handling dropdown box."""

        self.__multi_page_handling_dropdown_box.GetValue()

    def get_input_mode_dropdown_box(self):
        """Gets the value of the input mode dropdown box."""

        self.__input_mode_dropdown_box.GetValue()

    def get_autoprocessing_checkbox(self):
        """Gets the boolean status of the autoprocessing checkbox."""

        self.__autoprocessing_checkbox.GetValue()

    def set_paperwork_type(self, paperwork_type):
        """Sets the value of the paperwork type dropdown box."""

        self.__paperwork_type_dropdown_box.SetValue(paperwork_type)

    def set_multi_page_handling(self, multi_page_handling_option):
        """Sets the value of the multi-page handling dropdown box."""

        self.__multi_page_handling_dropdown_box.SetValue(
            multi_page_handling_option)

    def set_input_mode_dropdown_box(self, input_mode):
        """Sets the value of the input mode dropdown box."""

        self.__input_mode_dropdown_box.SetValue(input_mode)

    def set_autoprocessing_checkbox(self, autoprocessing_mode):
        """Sets the boolean status of the autoprocessing checkbox."""

        self.__autoprocessing_checkbox.SetValue(autoprocessing_mode)
