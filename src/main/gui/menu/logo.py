import wx
from wx.lib.statbmp import GenStaticBitmap

from src.main import file_system

class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Logo, self).__init__(parent)

        image_dir = file_system.image_resources_directory()
        image_path = image_dir + "\\logo.png"
        image = wx.Image(image_path, wx.BITMAP_TYPE_PNG)

        self.bitmap_ctrl = GenStaticBitmap(
            parent=self, ID=-1, bitmap=image.ConvertToBitmap(depth=32))

        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.sizer.AddStretchSpacer(prop=1)

        self.sizer.Add(
            window=self.bitmap_ctrl, proportion=1,
            flag=wx.ALIGN_BOTTOM|wx.ALL, border=15
        )

        self.sizer.AddStretchSpacer(prop=1)
        self.SetSizer(self.sizer)

        self.SetBackgroundColour(colour=wx.RED)