import wx
from gui.mainmenu.panels.panel import Panel

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

        self.__text_console_output_box = wx.TextCtrl(
            self,
            size = (835, 230),
            pos = (0, 0),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE
        )

        self.__text_console_output_box.SetBackgroundColour("LIGHT GREY")

    def write_log(self, text):
        """Writes a string of text to the console output log."""

        self.__text_console_output_box.write(text)