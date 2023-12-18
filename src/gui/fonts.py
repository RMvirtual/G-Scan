import wx


def font(point_size: int, bold: bool = False) -> wx.Font:
    return wx.Font(_font_info(point_size, bold))


def _font_info(point_size: int, bold: bool = False) -> wx.FontInfo:
    result = wx.FontInfo(pointSize=point_size)

    if bold:
        result.Bold()

    return result
