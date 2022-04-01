import wx


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        img = wx.Image(200, 200)

        self._image = wx.StaticBitmap(
            parent=self, bitmap=wx.Bitmap(img))

        self._image.SetScaleMode(wx.StaticBitmap.Scale_AspectFit)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._image, 0, wx.SHAPED)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)

    def setImage(self, image_path: str) -> None:
        img = wx.Image(image_path)

        img_width = img.GetWidth()
        img_height = img.GetHeight()

        max_size = self.GetSize().width

        if img_width > img_height:
            new_img_width = max_size
            new_img_height = max_size * img_height / img_width
        else:
            new_img_height = max_size
            new_img_width = max_size * img_width / img_height

        img = img.Scale(new_img_width, new_img_height)

        self._image.SetBitmap(wx.Bitmap(img))
