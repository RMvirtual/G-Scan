import wx

class Image(wx.StaticBitmap):
    """A class for an image."""

    def __init__(self, panel, image_path: str):
        """Creates a new image."""

        image_bitmap = wx.Bitmap(wx.Image(
            image_path, wx.BITMAP_TYPE_ANY))

        super().__init__(panel, wx.ID_ANY, image_bitmap)