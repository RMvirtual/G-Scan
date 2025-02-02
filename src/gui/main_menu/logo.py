import wx

import file_system


class LogoPanel(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        image = file_system.image_resources_directory().joinpath("logo.png")
        self.image = wx.Image(str(image), wx.BITMAP_TYPE_PNG)

        self.bitmap = wx.StaticBitmap(
            self, bitmap=self.image.ConvertToBitmap(depth=32))

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self.bitmap, proportion=0, flag=wx.EXPAND, border=0)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def on_resize(self, event: wx.Event) -> None:
        image_ratio = float(self.image.GetWidth()) / float(self.image.GetHeight())

        width, height = self.Size
        requested_ratio = float(width) / float(height)
        is_too_wide = requested_ratio > image_ratio

        if is_too_wide:
            new_width, new_height = map(int, (height*image_ratio, height))
        
        else:
            new_width, new_height = map(int, (width, width/image_ratio))
        
        scaled_image: wx.Image = self.image.Scale(
            new_width, new_height, wx.IMAGE_QUALITY_NORMAL)

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())
