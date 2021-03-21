from gui.widgets.panel import Panel
from gui.mainmenu.panels.toppanel.file_panel import FilePanel
from gui.mainmenu.panels.toppanel.user_settings_panel import UserSettingsPanel

class TopPanel(Panel):
    """A class for the top panel of the main menu GUI."""

    def __init__(self, frame):
        """Creates a new top panel."""

        print("Gets here in top panel")
        super().__init__(frame, (840, 255), (10, 10))

        print("Gets past superclass constructor in top panel.")
        self.__create_widgets()

    def __create_widgets(self):
        """Creates the top-panel's sub-panels and underlying 
        widgets.
        """

        self.__file_panel = FilePanel(self)
        self.__user_settings_panel = UserSettingsPanel(self)