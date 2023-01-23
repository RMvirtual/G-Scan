import wx
from wx.lib.floatcanvas import FloatCanvas

from src.main.gui.app import screen_size
from src.main.gui.image_viewer.panels.image import BitmapViewer
from src.main.gui.image_viewer.panels.input import InputPanel
from src.main.gui.image_viewer.panels.navigation import NavigationPanel

class ImageViewer(wx.Frame):
    def __init__(self, title: str):
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)
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

    def bind_exit(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._navigation_panel.exit)

    def bind_bitmap_movement(self, callback):
        self._nav_canvas.Canvas.Bind(FloatCanvas.EVT_MOTION, callback)

    def bind_submit(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._input_panel.submit)

    def bind_skip(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._input_panel.skip)

    def bind_split(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._input_panel.split)

    @property
    def status_bar(self) -> str:
        return self.GetStatusText()

    @status_bar.setter
    def status_bar(self, new_status: str) -> None:
        self.SetStatusText(new_status)
