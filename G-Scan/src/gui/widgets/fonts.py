import wx

def getCalibriFont(size: int) -> wx.Font:
    """Gets a Calibri font at a specific size."""

    return getFont("calibri", size)

def getFont(font: str, size: int) -> wx.Font:
    """Creates a font to be used."""

    font = wx.Font(
        size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, font)

    return font