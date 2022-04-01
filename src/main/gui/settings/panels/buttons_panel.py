from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.buttons import Button
from src.main.gui.widgets.widget import Attributes


class ButtonsPanel(Panel):
    def __init__(self, frame):
        super().__init__(frame, (860, 30), (10, 195))
        self.__create_buttons()

    def __create_buttons(self):
        self.__create_save_button()
        self.__create_cancel_button()

    def __create_save_button(self) -> None:
        attributes = self.__create_save_button_attributes()
        self.__save_button = Button.from_attributes(attributes)

    def __create_save_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Save"
        attributes.size = (60, 25)
        attributes.position = (200, 0)

        return attributes

    def __create_cancel_button(self) -> None:
        attributes = self.__create_cancel_button_attributes()
        self.__cancel_button = Button.from_attributes(attributes)

    def __create_cancel_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Cancel"
        attributes.size = (60, 25)
        attributes.position = (270, 0)

        return attributes

    def set_save_button_function(self, callback_function):
        self.__save_button.bind_function_to_click(callback_function)

    def set_cancel_button_function(self, callback_function):
        self.__cancel_button.bind_function_to_click(callback_function)