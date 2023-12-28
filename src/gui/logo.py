import wx
import file_system

import gui.metrics


class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        image = file_system.image_resources_directory().joinpath("logo.png")
        self.image = wx.Image(str(image), wx.BITMAP_TYPE_PNG)

        self.bitmap = wx.StaticBitmap(
            self, bitmap=self.image.ConvertToBitmap(depth=32))

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self.bitmap, proportion=0, flag=wx.EXPAND, border=0)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def on_resize(self, _event = None) -> None:
        width, height = self.Size
        
        new_width, new_height = gui.metrics.scale_with_ratio(
            self.image, width, height)

        scaled_image = self.image.Scale(
            int(new_width), int(new_height), wx.IMAGE_QUALITY_NORMAL)

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())
