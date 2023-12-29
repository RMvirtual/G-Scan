import wx


def aspect_ratio(width: int, height: int) -> float:
    return float(width) / float(height)


def scale_to_ratio(ratio: float, width: int, height: int) -> tuple[int, int]:
    too_wide = aspect_ratio(width, height) > ratio

    return (height * ratio, height) if too_wide else (width, width / ratio)

def scale_with_ratio(
        image: wx.Image, new_width: int, new_height: int) -> tuple[int, int]:
    return scale_to_ratio(image_aspect_ratio(image), new_width, new_height)


def image_aspect_ratio(image: wx.Image) -> float:
    return aspect_ratio(image.GetWidth(), image.GetHeight())


def recommended_metrics() -> tuple[tuple[int, int], wx.Point]:
    size = scaled_sizes()

    return size, wx.Point(x=size[0], y=0)


def scaled_sizes() -> tuple[int, int]:
    width, height = wx.DisplaySize()

    return int(width/2), int(height/1.1)
