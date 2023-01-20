from .panels.image import ImagePanel
from .panels.input import InputPanel
from .panels.navigation import NavigationPanel
import wx


class ImageViewer(wx.Frame):
    def __init__(self):
        display_size = wx.DisplaySize()
        width = display_size[0]/2
        height = display_size[1]

        super().__init__(
            parent=None, title="Paperwork Viewer", size=(width, height)
        )
        self._initialise_widgets()
        self.Show()

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def _initialise_widgets(self) -> None:
        self._initialise_panels()
        self._initialise_sizer()

    def _initialise_panels(self) -> None:
        self._input_panel = InputPanel(self)
        self._image_panel = ImagePanel(self)
        self._navigation_panel = NavigationPanel(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Frame is blue colour.
        sizer.Add(self._input_panel, 0, flag=wx.EXPAND)  # Yellow
        sizer.Add(self._image_panel, 1, flag=wx.EXPAND)  # Red
        sizer.Add(self._navigation_panel, 0, flag=wx.EXPAND)  # Green

        # sizer.SetSizeHints(self)
        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.BLUE)

    def set_image(self, image: wx.Image) -> None:
        self._image_panel.set_image(image)

    def set_bitmap(self, bitmap: wx.Bitmap) -> None:
        self._image_panel.set_bitmap(bitmap)

    def on_resize(self, event: wx.Event):
        event.Skip()

    def set_submit_callback(self, callback) -> None:
        self._input_panel.bind_submit_callback(callback)

    def set_skip_callback(self, callback) -> None:
        self._input_panel.bind_skip_callback(callback)

    def set_split_callback(self, callback) -> None:
        self._input_panel.bind_split_callback(callback)

    def set_exit_callback(self, callback) -> None:
        self._navigation_panel.set_exit_callback(callback)

    def close(self, event: any = None) -> None:
        self.Close()

    @property
    def image_panel_size(self):
        return self._image_panel.size
