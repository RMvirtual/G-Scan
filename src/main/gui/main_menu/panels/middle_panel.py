from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.buttons import Button, ImageButton
from src.main.gui.widgets.text import TextLabel
from src.main.gui.widgets.widget import Attributes
import src.main.file_system.file_system as file_system
import src.main.gui.widgets.fonts as fonts


class MiddlePanel(Panel):
    def __init__(self, frame):
        super().__init__(frame, size=(850, 30), position=(10, 265))
        self.__create_toolbar_widgets()

    def __create_toolbar_widgets(self):
        self.__create_start_button()
        self.__create_quick_mode_preview_text()
        self.__create_michelin_man_button()
        self.__create_settings_button()
        self.__create_exit_button()

    def __create_start_button(self) -> None:
        attributes = self.__create_start_button_attributes()
        self.__start_button = Button.from_attributes(attributes)

    def __create_start_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Start"
        attributes.size = (60, 25)
        attributes.position = (0, 0)

        return attributes

    def __create_quick_mode_preview_text(self) -> None:
        attributes = self.__create_quick_mode_preview_text_attributes()
        self.__quick_mode_preview_text = TextLabel.from_attributes(attributes)
        self.__quick_mode_preview_text.SetFont(fonts.getCalibriFont(12))

    def __create_quick_mode_preview_text_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (180, 14)
        attributes.position = (155, 3)

        return attributes

    def __create_michelin_man_button(self):
        attributes = self.__create_michelin_man_button_attributes()
        self.__michelin_man_button = ImageButton.from_attributes(attributes)

    def __create_michelin_man_button_attributes(self) -> Attributes:
        michelin_man_logo_path = (
            file_system.image_resources_directory() + "\\michelin_logo.jpg")

        attributes = self.create_empty_attributes()

        attributes.image_path = michelin_man_logo_path
        attributes.scaling_factor = (20, 20)
        attributes.size = (25, 25)
        attributes.position = (680, 0)

        return attributes

    def __create_settings_button(self) -> None:
        attributes = self.__create_settings_button_attributes()
        self.__settings_button = Button.from_attributes(attributes)

    def __create_settings_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Settings"
        attributes.size = (60, 25)
        attributes.position = (710, 0)

        return attributes

    def __create_exit_button(self) -> None:
        attributes = self.__create_exit_button_attributes()
        self.__exit_button = Button.from_attributes(attributes)

    def __create_exit_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Exit"
        attributes.size = (60, 25)
        attributes.position = (775, 0)

        return attributes

    def set_quick_mode_hint_text(self, text):
        self.__quick_mode_preview_text.SetLabel(text)

    def set_start_button_function(self, callback_function):
        self.__start_button.bind_function_to_click(callback_function)

    def set_exit_button_function(self, callback_function):
        self.__exit_button.bind_function_to_click(callback_function)

    def set_settings_button_function(self, callback_function):
        self.__settings_button.bind_function_to_click(callback_function)

    def set_michelin_man_button_function(self, callback_function):
        self.__michelin_man_button.bind_function_to_click(callback_function)
