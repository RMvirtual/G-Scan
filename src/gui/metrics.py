import wx


def preserved_scale(image: wx.Image, width: int, height: int) -> tuple[int, int]:
    image_ratio = float(image.GetWidth()) / float(image.GetHeight())
    requested_ratio = float(width) / float(height)
    is_too_wide = requested_ratio > image_ratio

    if is_too_wide:
        return (height*image_ratio, height)
    
    return (width, width/image_ratio)
