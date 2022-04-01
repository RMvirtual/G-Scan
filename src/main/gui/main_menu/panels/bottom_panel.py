from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.text import TextConsole


class BottomPanel(Panel):
    """Bottom panel for the main menu GUI."""

    def __init__(self, frame):
        """Creates a new bottom panel for the main menu GUI."""

        super().__init__(
            frame,
            size=(840, 230),
            position=(10, 295)
        )

        self.__create_text_console()

    def __create_text_console(self):
        """Creates a text console display output box."""

        self.__text_console_output_box = TextConsole(
            self, (835, 230), (0, 0))

    def write_log(self, text):
        """Writes a string of text to the console output log."""

        self.__text_console_output_box.write(text)
