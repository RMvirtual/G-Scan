import wx

def getCalibriFont(size: int) -> wx.Font:
    """Gets a Calibri font at a specific size."""

    return getFont("calibri", size)

def getFont(font: str, size: int) -> wx.Font:
    """Creates a font to be used."""

    font = wx.Font(
        pointSize=size, family=wx.MODERN, style=wx.NORMAL, weight=wx.NORMAL,
        underline=False, facename=font
    )

    return font