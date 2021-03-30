from gui.widgets.panel import Panel
from gui.widgets.text import TextLabel
from gui.widgets.dropdownboxes import DropdownBox
from gui.widgets.checkboxes import CheckBox
from gui.widgets.widget import Attributes

class ModeOptionsPanel(Panel):
    """A class representing the mode options panel."""

    def __init__(self, frame):
        super().__init__(frame, (860, 50), (10, 135))

        self.__create_paperwork_type_widgets()
        self.__create_multi_page_handling_widgets()
        self.__create_input_mode_widgets()
        self.__create_autoprocessing_checkbox()

    def __create_paperwork_type_widgets(self) -> None:
        """Creates widgets related to the default paperwork type
        value."""

        self.__create_paperwork_type_label()
        self.__create_paperwork_type_dropdown_box()

    def __create_multi_page_handling_widgets(self) -> None:
        """Creates widgets related to the default value for
        multi-page handling."""

        self.__create_multi_page_handling_label()
        self.__create_multi_page_handling_dropdown_box()

    def __create_input_mode_widgets(self) -> None:
        """Creates widgets related to the default user input mode."""

        self.__create_input_mode_label()
        self.__create_input_mode_dropdown_box()

    def __create_paperwork_type_dropdown_box(self) -> None:
        """Creates the paperwork type dropdown box."""

        attributes = self.__create_paperwork_type_dropdown_box_attributes()
        
        self.__paperwork_type_dropdown_box = (
            DropdownBox.from_attributes(attributes))

    def __create_paperwork_type_dropdown_box_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the paperwork
        type dropdown box."""

        attributes = self.create_empty_attributes()

        attributes.text = "lol"
        attributes.options = ["Customer PW", "Loading List", "POD"]
        attributes.size = (120, 25)
        attributes.position = (200, 0)

        return attributes

    def __create_paperwork_type_label(self) -> None:
        """Creates the paperwork type label."""

        attributes = self.__create_paperwork_type_label_attributes()
        self.__paperwork_type_label = TextLabel.from_attributes(attributes)

    def __create_paperwork_type_label_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the paperwork
        type label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Default Paperwork Type:"
        attributes.size = (200, 20)
        attributes.position = (0, 0)

        return attributes

    def __create_multi_page_handling_label(self) -> None:
        """Creates the multi-page handling label."""

        attributes = self.__create_multi_page_handling_label_attributes()
        
        self.__multi_page_handling_label = (
            TextLabel.from_attributes(attributes))

    def __create_multi_page_handling_label_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the
        multi-page handling label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Multi-Page Handling:"
        attributes.size = (165, 20)
        attributes.position = (330, 0)

        return attributes

    def __create_multi_page_handling_dropdown_box(self) -> None:
        """Creates the multi-page handling dropdown box."""

        attributes = (
            self.__create_multi_page_handling_dropdown_box_attributes())
        
        self.__multi_page_handling_dropdown_box = (
            DropdownBox.from_attributes(attributes))

    def __create_multi_page_handling_dropdown_box_attributes(self) \
            -> Attributes:
        """Creates the attributes required to instantiate the
        multi-page handling dropdown box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "lol"
        attributes.options = ["Do Not Split", "Split"]
        attributes.size = (120, 25)
        attributes.position = (500, 0)

        return attributes

    def __create_input_mode_label(self) -> None:
        """Creates the input mode label."""

        attributes = self.__create_input_mode_label_attributes()
        self.__input_mode_label = TextLabel.from_attributes(attributes)

    def __create_input_mode_label_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the
        input mode label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Input Mode"
        attributes.size = (80, 20)
        attributes.position = (630, 0)

        return attributes

    def __create_input_mode_dropdown_box(self) -> None:
        """Creates the input mode dropdown box."""

        attributes = self.__create_input_mode_dropdown_box_attributes()
        
        self.__input_mode_dropdown_box = (
            DropdownBox.from_attributes(attributes))

    def __create_input_mode_dropdown_box_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the
        input mode dropdown box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "lol"
        attributes.options = ["Normal", "Quick"]
        attributes.size = (120, 25)
        attributes.position = (735, 0)

        return attributes

    def __create_autoprocessing_checkbox(self) -> None:
        """Creates the autoprocessing checkbox."""

        attributes = self.__create_autoprocessing_checkbox_attributes()
        self.__autoprocessing_checkbox = CheckBox.from_attributes(attributes)

    def __create_autoprocessing_checkbox_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the
        input mode dropdown box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "POD Autoprocessing"
        attributes.size = (160, 25)
        attributes.position = (200, 23)

        return attributes

    def get_paperwork_type(self):
        """Gets the value of the paperwork type dropdown box."""

        return self.__paperwork_type_dropdown_box.GetValue()

    def get_multi_page_handling(self):
        """Gets the value of the multi-page handling dropdown box."""

        return self.__multi_page_handling_dropdown_box.GetValue()

    def get_input_mode(self):
        """Gets the value of the input mode dropdown box."""

        return self.__input_mode_dropdown_box.GetValue()

    def get_autoprocessing_mode(self):
        """Gets the boolean status of the autoprocessing checkbox."""

        return self.__autoprocessing_checkbox.GetValue()

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
