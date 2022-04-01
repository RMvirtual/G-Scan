from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.buttons import Button, ImageButton
from src.main.gui.widgets.text import TextLabel
from src.main.gui.widgets.widget import Attributes
import src.main.file_system.file_system as file_system
import src.main.gui.widgets.fonts as fonts


class MiddlePanel(Panel):
    """Middle panel for the main menu GUI."""

    def __init__(self, frame):
        """Creates a new middle panel for the main menu GUI."""

        super().__init__(
            frame,
            size=(850, 30),
            position=(10, 265)
        )

        self.__create_toolbar_widgets()

    def __create_toolbar_widgets(self):
        """Creates widgets related to the middle toolbar."""

        self.__create_start_button()
        self.__create_quick_mode_preview_text()
        self.__create_michelin_man_button()
        self.__create_settings_button()
        self.__create_exit_button()

    def __create_start_button(self) -> None:
        """Creates the start button."""

        attributes = self.__create_start_button_attributes()
        self.__start_button = Button.from_attributes(attributes)

    def __create_start_button_attributes(self) -> Attributes:
        """Creates the attributes data required for the start button."""

        attributes = self.create_empty_attributes()

        attributes.text = "Start"
        attributes.size = (60, 25)
        attributes.position = (0, 0)

        return attributes

    def __create_quick_mode_preview_text(self) -> None:
        """Creates the quick mode preview text widget."""

        attributes = self.__create_quick_mode_preview_text_attributes()
        self.__quick_mode_preview_text = TextLabel.from_attributes(attributes)
        self.__quick_mode_preview_text.SetFont(fonts.getCalibriFont(12))

    def __create_quick_mode_preview_text_attributes(self) -> Attributes:
        """Creates the attribute data required for the quick mode
        preview text.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (180, 14)
        attributes.position = (155, 3)

        return attributes

    def __create_michelin_man_button(self):
        """Creates the michelin man button."""

        attributes = self.__create_michelin_man_button_attributes()
        self.__michelin_man_button = ImageButton.from_attributes(attributes)

    def __create_michelin_man_button_attributes(self) -> Attributes:
        """Creates the attributes required for instantiating the
        Michelin Man button.
        """

        michelin_man_logo_path = (
                file_system.resources_directory()
                + "images\\michelin_logo.jpg"
        )

        attributes = self.create_empty_attributes()

        attributes.image_path = michelin_man_logo_path
        attributes.scaling_factor = (20, 20)
        attributes.size = (25, 25)
        attributes.position = (680, 0)

        return attributes

    def __create_settings_button(self) -> None:
        """Creates the settings button."""

        attributes = self.__create_settings_button_attributes()
        self.__settings_button = Button.from_attributes(attributes)

    def __create_settings_button_attributes(self) -> Attributes:
        """Creates the attributes for instantiating the settings
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Settings"
        attributes.size = (60, 25)
        attributes.position = (710, 0)

        return attributes

    def __create_exit_button(self) -> None:
        """Creates the exit button."""

        attributes = self.__create_exit_button_attributes()
        self.__exit_button = Button.from_attributes(attributes)

    def __create_exit_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the exit
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Exit"
        attributes.size = (60, 25)
        attributes.position = (775, 0)

        return attributes

    def set_quick_mode_hint_text(self, text):
        """Overwrites the text found in the quick mode hint text
        box."""

        self.__quick_mode_preview_text.SetLabel(text)

    def set_start_button_function(self, callback_function):
        """Sets the function to be run when the start button is
        clicked."""

        self.__start_button.bind_function_to_click(callback_function)

    def set_exit_button_function(self, callback_function):
        """Sets the function to be run when the exit button is
        clicked."""

        self.__exit_button.bind_function_to_click(callback_function)

    def set_settings_button_function(self, callback_function):
        """Sets the function to be run when the settings button is
        clicked."""

        self.__settings_button.bind_function_to_click(callback_function)

    def set_michelin_man_button_function(self, callback_function):
        """Sets the function to be run when the michelin man button is
        clicked."""

        self.__michelin_man_button.bind_function_to_click(callback_function)
