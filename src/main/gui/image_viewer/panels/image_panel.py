import wx


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        self._image = wx.StaticBitmap(parent=self)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._image, 0, wx.SHAPED)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)
