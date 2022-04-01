import wx
from src.main.images.image_conversion import toScaledImage

class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)
        img = wx.Image(200, 200)

        self._image = wx.StaticBitmap(
            parent=self, bitmap=wx.Bitmap(img))

        self._image.SetScaleMode(wx.StaticBitmap.Scale_Fill)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._image, 0, wx.SHAPED)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)

    def setImage(self, image_path: str) -> None:
        size = self.GetSize()
        img = toScaledImage(image_path, size.width, size.height)
        self._image.SetBitmap(wx.Bitmap(img))