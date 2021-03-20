import wx

class Widget():

    def __init__(self) -> None:
        """Creates a new widget."""

    def getCalibriFont(self, size: int) -> wx.Font:
        """Sets the current font to Calibri at a specific size."""

        return self.__create_font("calibri", size)

    def getFont(self, font: str, size: int) -> wx.Font:

        return self.__create_font(font, size)

    def __create_font(self, font: str, size: int) -> wx.Font:
        """Creates a font to be used."""

        font = wx.Font(
            size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, font)

        return font