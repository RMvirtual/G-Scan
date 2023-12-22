import wx


def font(point_size: int, bold: bool = False) -> wx.Font:
    result = wx.FontInfo(pointSize=point_size)

    if bold:
        result.Bold()

    return wx.Font(result)
