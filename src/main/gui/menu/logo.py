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

        self.bitmap_ctrl = wx.StaticBitmap(
            parent=self, bitmap = self.image.ConvertToBitmap(depth=32))

        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizer.Add(
            window=self.bitmap_ctrl, proportion=1,
            flag=wx.ALL, border=15
        )

        self.SetSizerAndFit(self.sizer)

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.SetBackgroundColour(colour=wx.RED)

    def on_resize(self, event) -> None:
        panel_width, panel_height = self.Size

        new_width, new_height = aspect_ratio.scale_with_ratio(
            image=self.image, new_width=panel_width, new_height=panel_height)

        scaled_image = self.image.Scale(
            width=new_width, height=new_height,
            quality=wx.IMAGE_QUALITY_NORMAL
        )

        self.bitmap_ctrl.SetBitmap(scaled_image.ConvertToBitmap())
