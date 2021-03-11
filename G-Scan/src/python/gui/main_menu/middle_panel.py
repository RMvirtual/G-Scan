import wx
from app import file_system

class MiddlePanel(wx.Panel):
    """Middle panel for the main menu GUI."""

    def __init__(self, frame):
        """Creates a new middle panel for the main menu GUI."""

        super().__init__(
            frame,
            size = (850, 30),
            pos = (10, 265)
        )

        self.__frame = frame
        self.__set_fonts()
        self.__create_toolbar_widgets()
        
    def __set_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = self.__create_font(11)
        self.__body_font = self.__create_font(14)

    def __create_font(self, font_size):
        """Creates a calibri font to be used."""

        font = wx.Font(
            font_size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        return font

    def __create_toolbar_widgets(self):
        """Creates widgets related to the middle toolbar."""

        # Start button.
        self.__start_button = wx.Button(
            self,
            label = "Start",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__start_button.SetFont(self.__button_font)

        self.__start_button.Bind(
            wx.EVT_BUTTON,
            self.__start_button_click
        )

        # Quick Mode user aid message for displaying a preview of the
        # output that quick mode will calculate based on the current
        # user settings and what they have entered so far in the user
        # input entry box.
        self.__quick_mode_preview_text = wx.StaticText(
            self,
            label = "",
            size = (180, 14),
            pos = (155, 3),
            style = wx.ALIGN_RIGHT
        )

        self.__quick_mode_preview_text.SetFont(wx.Font(
            12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

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

        # Settings button.
        self.__settings_button = wx.Button(
            self,
            label = "Settings",
            size = (60, 25),
            pos = (710, 0)
        )

        self.__settings_button.SetFont(self.__button_font)

        self.__settings_button.Bind(
            wx.EVT_BUTTON,
            self.__settings_button_click
        )

        # Exit button.
        self.__exit_button = wx.Button(
            self,
            label = "Exit",
            size = (60, 25),
            pos = (775, 0)
        )

        self.__exit_button.SetFont(self.__button_font)

        self.__exit_button.Bind(
            wx.EVT_BUTTON,
            self.__exit_button_click
        )

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
