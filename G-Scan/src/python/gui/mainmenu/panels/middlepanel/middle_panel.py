import wx
from gui.widgets.panel import Panel
from gui.widgets.buttons import Button
from app import file_system
from gui.widgets.text import TextLabel

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

        self.__start_button = Button(self, "Start", (60, 25), (0, 0))
        self.__start_button.bindFunctionToClick(self.__start_button_click)

        # Quick Mode user aid message for displaying a preview of the
        # output that quick mode will calculate based on the current
        # user settings and what they have entered so far in the user
        # input entry box.
        self.__quick_mode_preview_text = TextLabel(
            self, "", (180, 14), (155, 3))

        self.__quick_mode_preview_text.SetFont(
            self.__quick_mode_preview_text.getCalibriFont(12))

        # Michelin Man button.
        michelin_man_logo_path = (
            file_system.get_resources_directory() + "images\\michelin_logo.jpg")

        michelin_man_logo = wx.Image(
            michelin_man_logo_path, wx.BITMAP_TYPE_ANY).Scale(20, 20)
        
        self.__michelin_man_button = wx.BitmapButton(
            self,
            bitmap = michelin_man_logo.ConvertToBitmap(),
            size = (25, 25),
            pos = (680, 0)
        )

        self.__settings_button = Button(self, "Settings", (60, 25), (710, 0))
        self.__settings_button.bindFunctionToClick(
            self.__settings_button_click)

        self.__exit_button = Button(self, "Exit", (60, 25), (775, 0))
        self.__exit_button.bindFunctionToClick(
            self.__exit_button_click)

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
