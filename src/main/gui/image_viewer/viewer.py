from .panels.image import BitmapViewer
from .panels.input import InputPanel
from .panels.navigation import NavigationPanel
import wx


class ImageViewer(wx.Frame):
    def __init__(self):
        display_size = wx.DisplaySize()
        width = display_size[0] / 2
        height = display_size[1] / 1.1

        super().__init__(
            parent=None, title="Paperwork Viewer",
            size=(width, height), pos=wx.Point(x=width, y=0)
        )
        self._initialise_widgets()
        self.Show()

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def _initialise_widgets(self) -> None:
        self.CreateStatusBar()
        self._initialise_panels()
        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

    def _initialise_panels(self) -> None:
        self._input_panel = InputPanel(self)
        self._nav_canvas = BitmapViewer(self)
        self._navigation_panel = NavigationPanel(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(
            window=self._input_panel, proportion=0, flag=wx.EXPAND)
        sizer.Add(window=self._nav_canvas, proportion=1, flag=wx.EXPAND)
        sizer.Add(window=self._navigation_panel, proportion=0, flag=wx.EXPAND)
        self.SetSizer(sizer)

    def set_image(self, image: wx.Image) -> None:
        self._nav_canvas.load_image(image)

    def on_resize(self, _event: wx.Event):
        print("Resizing in viewer.")

    def set_submit_callback(self, callback) -> None:
        self._input_panel.bind_submit_callback(callback)

    def set_skip_callback(self, callback) -> None:
        self._input_panel.bind_skip_callback(callback)

    def set_split_callback(self, callback) -> None:
        self._input_panel.bind_split_callback(callback)

    def set_exit_callback(self, callback) -> None:
        self._navigation_panel.set_exit_callback(callback)

    def close(self, _event: wx.Event = None) -> None:
        self.Close()
