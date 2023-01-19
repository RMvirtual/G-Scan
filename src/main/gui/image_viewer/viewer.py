from .panels.image import ImagePanel
from .panels.input import InputPanel
from .panels.navigation import NavigationPanel
import wx


class ImageViewer(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Paperwork Viewer")
        self._initialise_widgets()
        self.Show()

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def _initialise_widgets(self) -> None:
        self._input_panel = InputPanel(self)
        self._image_panel = ImagePanel(self)
        self._navigation_panel = NavigationPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Frame is blue colour.
        sizer.Add(self._input_panel, 0, flag=wx.EXPAND)  # Yellow
        sizer.Add(self._image_panel, 1, flag=wx.EXPAND)  # Red
        sizer.Add(self._navigation_panel, 0, flag=wx.EXPAND)  # Green

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.BLUE)

    def set_image(self, image_path: str):
        self._image_panel.set_image(image_path)

    def on_resize(self, event: wx.Event):
        self._image_panel.resize_image()
        event.Skip()

    def set_pixelmap(self, pixmap):
        self._image_panel.set_pixel_map(pixmap)

    def set_exit_callback(self, callback) -> None:
        self._navigation_panel.set_exit_callback(callback)

    def close(self, event: any = None) -> None:
        self.Close()
