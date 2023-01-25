import wx
from wx.lib.statbmp import GenStaticBitmap

from src.main import file_system
from src.main.gui.app import aspect_ratio

class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Logo, self).__init__(parent)

        image_dir = file_system.image_resources_directory()
        image_path = image_dir + "\\logo.png"
        self.image = wx.Image(image_path, wx.BITMAP_TYPE_PNG)

        self.bitmap = wx.StaticBitmap(
            parent=self, bitmap = self.image.ConvertToBitmap(depth=32))

        self._initialise_sizer()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.SetBackgroundColour(colour=wx.RED)
        self.on_resize()

    def _initialise_sizer(self) -> None:
        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizer.Add(
            window=self.bitmap, proportion=0,
            flag=wx.ALL|wx.ALIGN_BOTTOM|wx.SHAPED, border=0
        )

        self.SetSizer(self.sizer)

    def on_resize(self, _event = None) -> None:
        panel_width, panel_height = self.Size

        new_width, new_height = aspect_ratio.scale_with_ratio(
            image=self.image, new_width=panel_width, new_height=panel_height)

        scaled_image = self.image.Scale(
            width=new_width, height=new_height,
            quality=wx.IMAGE_QUALITY_NORMAL
        )

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())
