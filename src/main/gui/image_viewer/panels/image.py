import wx


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        self._image_path = ""

        self._image_control = wx.StaticBitmap(
            parent=self, bitmap=wx.Bitmap(wx.Image(800, 800)))

        self._image_control.SetScaleMode(wx.StaticBitmap.Scale_AspectFit)

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._image_control, 0, wx.EXPAND)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)
        self.SetBackgroundColour(colour=wx.RED)
        self._pixel_map = None

    def set_image(self, image_path: str) -> None:
        self._image_path = image_path
        self.resize_image()

    def set_pixel_map(self, pix):
        self._pixel_map = pix
        bitmap = self._bitmap_from_pixel_map()
        self._image_control.SetBitmap(bitmap)

    def _bitmap_from_pixel_map(self) -> wx.Bitmap:
        if self._pixel_map.alpha:
            bitmap = wx.Bitmap.FromBufferRGBA(
                self._pixel_map.width,
                self._pixel_map.height,
                self._pixel_map.samples
            )

        else:
            bitmap = wx.Bitmap.FromBuffer(
                self._pixel_map.width,
                self._pixel_map.height,
                self._pixel_map.samples
            )

        return bitmap

    def resize_image(self):
        size = self.GetSize()

        """
        scaled_pixel_map = fitz.Pixmap(
            source=self._pixel_map, width=size.width, height=size.height,
            clip=None
        )

        self.set_pixel_map(scaled_pixel_map)
        """