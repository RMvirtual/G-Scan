import wx
from wx.lib.statbmp import GenStaticBitmap

from src.main import file_system

class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Logo, self).__init__(parent)

        image_dir = file_system.image_resources_directory()
        image_path = image_dir + "\\g-scan_logo.png"

        image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)

        self.bitmap_ctrl = GenStaticBitmap(
            parent=self, ID=-1, bitmap=image.ConvertToBitmap())
