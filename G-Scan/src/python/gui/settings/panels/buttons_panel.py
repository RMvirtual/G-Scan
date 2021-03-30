from gui.widgets.panel import Panel
from gui.widgets.buttons import Button
from gui.widgets.widget import Attributes

class ButtonsPanel(Panel):
    """A class representing the buttons panel."""

    def __init__(self, frame):
        super().__init__(
            frame, (860, 30), (10, 195))

        self.__create_buttons()

    def __create_buttons(self):
        """Creates widgets for the Save and Cancel buttons."""

        self.__create_save_button()
        self.__create_cancel_button()

    def __create_save_button(self) -> None:
        """Creates the save button."""

        attributes = self.__create_save_button_attributes()
        self.__save_button = Button.from_attributes(attributes)

    def __create_save_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the save
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Save"
        attributes.size = (60, 25)
        attributes.position = (200, 0)

        return attributes

    def __create_cancel_button(self) -> None:
        """Creates the cancel button."""

        attributes = self.__create_cancel_button_attributes()
        self.__cancel_button = Button.from_attributes(attributes)

    def __create_cancel_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the cancel
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Cancel"
        attributes.size = (60, 25)
        attributes.position = (270, 0)

        return attributes

    def set_save_button_function(self, callback_function):
        """Sets the function to be called when the save button is clicked."""

        self.__save_button.bind_function_to_click(callback_function)

    def set_cancel_button_function(self, callback_function):
        """Sets the function to be called when the cancel button is clicked."""

        self.__cancel_button.bind_function_to_click(callback_function)