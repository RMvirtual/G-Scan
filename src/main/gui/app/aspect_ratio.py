import wx


def aspectRatio(width: int, height: int) -> float:
    return float(width) / float(height)


def scale_to_ratio(ratio: float, width: int, height: int) -> tuple[int, int]:
    too_wide = aspectRatio(width, height) > ratio

    if too_wide:
        width = height * ratio

    else:
        height = width / ratio

    return width, height


def scale_with_ratio(
        image: wx.Image, new_width: int, new_height: int) -> tuple[int, int]:
    return scale_to_ratio(image_aspect_ratio(image), new_width, new_height)


def image_aspect_ratio(image: wx.Image) -> float:
    return aspectRatio(image.GetWidth(), image.GetHeight())
