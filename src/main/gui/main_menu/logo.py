import wx
from wx.lib.statbmp import GenStaticBitmap

from src.main import file_system
from src.main.gui.metrics import aspect_ratio


class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise_two()

    def _old_constructor(self) -> None:
        self._initialise_widgets()
        self._initialise_sizer()
        self.Bind(wx.EVT_SIZE, self.on_resize)

    def _initialise_two(self) -> None:
        image_dir = file_system.image_resources_directory()
        image_path = image_dir + "\\logo.png"
        self.SetBackgroundColour(wx.WHITE)

        self.bitmap = wx.Bitmap(name=image_path, type=wx.BITMAP_TYPE_ANY)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event: wx.EVT_PAINT) -> None:
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        gc = wx.GraphicsContext.Create(dc)
        bmp = gc.CreateBitmap(self.bitmap)
        gc.DrawBitmap(bmp=bmp, x=0, y=0, w=200, h=200)

    def _initialise_widgets(self) -> None:
        image_dir = file_system.image_resources_directory()
        image_path = image_dir + "\\logo.png"
        self.image = wx.Image(image_path, wx.BITMAP_TYPE_PNG)

        self.bitmap = wx.StaticBitmap(
            parent=self, bitmap = self.image.ConvertToBitmap(depth=32))

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND

        sizer.Add(window=self.bitmap, proportion=0, flag=flags, border=0)

        self.SetSizer(sizer)

    def on_resize(self, _event = None) -> None:
        print("In resize.")
        self.resize_logo()

    def resize_logo(self) -> None:
        width, height = self._scaled_image_metrics()
        scaled_image = self.image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())

    def _scaled_image_metrics(self) -> tuple[int, int]:
        width, height = self.Size

        return aspect_ratio.scale_with_ratio(self.image, width, height)
