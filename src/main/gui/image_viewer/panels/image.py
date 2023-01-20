import wx


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        self._image_control = wx.StaticBitmap(
            parent=self, bitmap=wx.Bitmap(wx.Image(800, 800)))

        self._image_control.SetScaleMode(wx.StaticBitmap.Scale_AspectFit)
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.RED)

    def _initialise_sizer(self) -> None:
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._image_control, 0, wx.EXPAND)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)

    def set_image(self, image: wx.Image) -> None:
        self._image_control.SetBitmap(image.ConvertToBitmap())

    def set_bitmap(self, bitmap: wx.Bitmap) -> None:
        self._image_control.SetBitmap(bitmap)

    @property
    def size(self) -> tuple[int, int]:
        """Tuple of size in pixels (x, y)."""
        return self._image_control.Size
