import wx


def preserved_scale(image: wx.Image, width: int, height: int) -> tuple[int, int]:
    image_ratio = float(image.GetWidth()) / float(image.GetHeight())
    requested_ratio = float(width) / float(height)
    is_too_wide = requested_ratio > image_ratio

    if is_too_wide:
        return (height*image_ratio, height)
    
    return (width, width/image_ratio)
    

def recommended_metrics() -> tuple[tuple[int, int], wx.Point]:
    width, height = wx.DisplaySize()
    size = int(width/2), int(height/1.1)

    return size, wx.Point(x=size[0], y=0)
