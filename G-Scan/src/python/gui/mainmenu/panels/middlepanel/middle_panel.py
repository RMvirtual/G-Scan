import wx
from gui.widgets.panel import Panel
from gui.widgets import fonts
from gui.widgets.buttons import Button
from app import file_system
from gui.widgets.text import TextLabel
from gui.widgets.widgetattributes import WidgetAttributes

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
        self.__start_button = Button.fromAttributes(attributes)

    def __create_start_button_attributes(self) -> WidgetAttributes:
        """Creates the attributes data required for the start button."""

        attributes = WidgetAttributes()

        attributes.parent_widget = self
        attributes.text = "Start"
        attributes.size = (60, 25)
        attributes.position = (0, 0)
        attributes.callback_function = self.__start_button_click

        return attributes

    def __create_quick_mode_preview_text(self) -> None:
        """Creates the quick mode preview text widget."""

        attributes = self.__create_quick_mode_preview_text_attributes()
        self.__quick_mode_preview_text = TextLabel.from_attributes(attributes)
        self.__quick_mode_preview_text.SetFont(fonts.getCalibriFont(12))

    def __create_quick_mode_preview_text_attributes(self) -> WidgetAttributes:
        """Creates the attribute data required for the quick mode
        preview text.
        """

        attributes = WidgetAttributes()

        attributes.parent_widget = self
        attributes.text = ""
        attributes.size = (180, 14)
        attributes.position = (155, 3)

        return attributes 

    def __create_michelin_man_button(self):
        """Creates the michelin man button."""

        michelin_man_logo_path = (
            file_system.get_resources_directory()
            + "images\\michelin_logo.jpg"
        )

        michelin_man_logo = wx.Image(
            michelin_man_logo_path, wx.BITMAP_TYPE_ANY).Scale(20, 20)
        
        self.__michelin_man_button = wx.BitmapButton(
            self,
            bitmap = michelin_man_logo.ConvertToBitmap(),
            size = (25, 25),
            pos = (680, 0)
        )

    def __create_settings_button(self) -> None:
        """Creates the settings button."""

        attributes = self.__create_settings_button_attributes()
        self.__settings_button = Button.fromAttributes(attributes)

    def __create_settings_button_attributes(self) -> WidgetAttributes:
        """Creates the attributes for instantiating the settings
        button.
        """

        attributes = WidgetAttributes()

        attributes.parent_widget = self
        attributes.text = "Settings"
        attributes.size = (60, 25)
        attributes.position = (710, 0)
        attributes.callback_function = self.__settings_button_click

        return attributes

    def __create_exit_button(self) -> None:
        """Creates the exit button."""

        attributes = self.__create_exit_button_attributes()
        self.__exit_button = Button.fromAttributes(attributes)

    def __create_exit_button_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the exit
        button.
        """

        attributes = WidgetAttributes()

        attributes.parent_widget = self
        attributes.text = "Exit"
        attributes.size = (60, 25)
        attributes.position = (775, 0)
        attributes.callback_function = self.__exit_button_click

        return attributes

    def __start_button_click(self, event = None):
        """Defines the behavior to follow when the start button
        is clicked on, activating the main application's start
        workflow method."""

        # self.__main_application.start()
        print("Start button clicked.")

    def __exit_button_click(self, event = None):
        """Defines the behaviour to follow when the exit button
        is clicked on, activating the main application's exit
        workflow method."""

        # self.__main_application.exit()
        print("Exit button clicked.")

    def __settings_button_click(self, event = None):
        """Defines the behaviour to follow when the exit button
        is clicked on, activating the main application's exit
        workflow method."""
        
        print("Settings button clicked.")
        # self.__main_application.open_settings_menu()

    def set_quick_mode_hint_text(self, text):
        """Overwrites the text found in the quick mode hint text
        box."""
        
        self.__quick_mode_preview_text.SetLabel(text)