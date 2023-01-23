from .panels.image import BitmapViewer
from .panels.input import InputPanel
from .panels.navigation import NavigationPanel
import wx
from wx.lib.floatcanvas import FloatCanvas


class ImageViewer(wx.Frame):
    def __init__(self):
        size, position = self._size_and_position

        super().__init__(
            parent=None, title="Paperwork Viewer",
            size=size, pos=position
        )

        self._initialise_widgets()
        self.Show()

    def _initialise_widgets(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("HELLO WORLD")
        self._initialise_panels()
        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

    def _initialise_panels(self) -> None:
        self._input_panel = InputPanel(self)
        self._nav_canvas = BitmapViewer(self)
        self._navigation_panel = NavigationPanel(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(window=self._input_panel, proportion=0, flag=wx.EXPAND)
        sizer.Add(window=self._nav_canvas, proportion=1, flag=wx.EXPAND)
        sizer.Add(window=self._navigation_panel, proportion=0, flag=wx.EXPAND)
        self.SetSizer(sizer)

    def close(self, _event: wx.Event = None) -> None:
        self.Close()

    def set_image(self, image: wx.Image) -> None:
        self._nav_canvas.load_image(image)

    def set_submit_callback(self, callback) -> None:
        self._input_panel.bind_submit_callback(callback)

    def set_skip_callback(self, callback) -> None:
        self._input_panel.bind_skip_callback(callback)

    def set_split_callback(self, callback) -> None:
        self._input_panel.bind_split_callback(callback)

    def set_exit_callback(self, callback) -> None:
        self._navigation_panel.set_exit_callback(callback)

    def set_bitmap_movement_callback(self, callback):
        self._nav_canvas.Canvas.Bind(FloatCanvas.EVT_MOTION, callback)

    @property
    def status_bar(self) -> str:
        return ""

    @status_bar.setter
    def status_bar(self, new_status: str) -> None:
        self.SetStatusText(new_status)

    @property
    def _size_and_position(self) -> tuple[tuple[int, int], wx.Point]:
        size = self._width_and_height

        return size, wx.Point(x=size[0], y=0)

    @property
    def _width_and_height(self) -> tuple[int, int]:
        width, height = wx.DisplaySize()

        return width/2, height/1.1