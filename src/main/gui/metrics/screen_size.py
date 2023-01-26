import wx


def recommended_metrics() -> tuple[tuple[int, int], wx.Point]:
    size = scaled_sizes()

    return size, wx.Point(x=size[0], y=0)


def scaled_sizes() -> tuple[int, int]:
    width, height = wx.DisplaySize()

    return width/2, height/1.1