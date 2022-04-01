import wx
from src.main.images.image_conversion import toScaledImagePreserveAspectRatio


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        self._image = wx.StaticBitmap(
            parent=self, bitmap=wx.Bitmap(wx.Image(200, 200)))

        self._image.SetScaleMode(wx.StaticBitmap.Scale_AspectFit)

        self._sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(self._image, 0, wx.EXPAND)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)
        self.SetBackgroundColour(colour=wx.RED)

    def setImage(self, image_path: str) -> None:
        size = self.GetSize()

        img = toScaledImagePreserveAspectRatio(
            image_path, size.width, size.height)

        self._image.SetBitmap(wx.Bitmap(img))
