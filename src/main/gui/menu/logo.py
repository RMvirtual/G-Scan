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

        self.on_resize()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.ALIGN_CENTRE_HORIZONTAL

        sizer.AddStretchSpacer()
        sizer.Add(window=self.bitmap, proportion=0, flag=flags, border=0)
        sizer.AddStretchSpacer()

        self.SetSizer(sizer)

    def on_resize(self, _event = None) -> None:
        width, height = self._scaled_image_metrics()
        scaled_image = self.image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())

    def _scaled_image_metrics(self) -> tuple[int, int]:
        width, height = self.Size

        return aspect_ratio.scale_with_ratio(self.image, width, height)
