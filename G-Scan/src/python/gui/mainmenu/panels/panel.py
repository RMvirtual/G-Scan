import wx

class Panel(wx.Panel):
    """A basic GUI panel (to be extended further into more concrete
    panels).
    """

    def __init__(self, frame, size, position):
        """Creates a new panel and attaches it to a frame."""

        super().__init__(
            frame,
            size = size,
            pos = position
        )

        self.__frame = frame
        self.__set_fonts()

    def __set_fonts(self):
        """Sets the fonts to be used for the widget types."""

        self.__button_font = self.__create_font(11)
        self.__body_font = self.__create_font(14)

    def __create_font(self, font_size):
        """Creates a calibri font to be used."""

        font = wx.Font(
            font_size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri")

        return font

    def get_button_font(self):
        """Returns the font required for most buttons."""

        return self.__button_font

    def get_body_font(self):
        """Returns the font required for most body text size items."""

        return self.__body_font