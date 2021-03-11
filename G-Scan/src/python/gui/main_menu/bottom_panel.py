import wx
from app import file_system

class BottomPanel(wx.Panel):
    """Bottom panel for the main menu GUI."""

    def __init__(self, frame):
        """Creates a new bottom panel for the main menu GUI."""

        super().__init__(
            frame,
            size = (840, 230),
            pos = (10, 295)
        )

        self.__frame = frame
        self.__set_fonts()

        # Text console display.
        self.__text_console_output_box = wx.TextCtrl(
            self,
            size = (835, 230),
            pos = (0, 0),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE
        )

        self.__text_console_output_box.SetBackgroundColour("LIGHT GREY")

    def __set_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = self.__create_font(11)
        self.__body_font = self.__create_font(14)

    def __create_font(self, font_size):
        """Creates a calibri font to be used."""

        font = wx.Font(
            font_size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        return font

    def write_log(self, text):
        """Writes a string of text to the console output log."""

        self.__text_console_output_box.write(text)