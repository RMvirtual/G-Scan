import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)
        self._initialise_canvas()
        self._initialise_bindings()

        self.SetBackgroundColour(colour=wx.RED)

    def _initialise_canvas(self) -> None:
        self._nav_canvas = NavCanvas.NavCanvas(
            self,
            ProjectionFun=None,
            BackgroundColor=wx.LIGHT_GREY
        )

        self._canvas = self._nav_canvas.Canvas

        # self._canvas.MaxScale = 20

    def _initialise_bindings(self) -> None:
        self._canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self._canvas.Bind(wx.EVT_LEFT_DCLICK, self.zoom_to_fit)
        self._canvas.Bind(wx.EVT_SIZE, self.on_resize)

    def set_image(self, image: wx.Image) -> None:
        scaled_bitmap = FloatCanvas.ScaledBitmap2(
            image,
            (0, 0),
            Height=image.GetHeight(),
            Position="tl"
        )

        self._canvas.AddObject(scaled_bitmap)
        self._canvas.Draw()
        self._canvas.ZoomToBB()

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self._canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def zoom_to_fit(self, _event: wx.EVT_LEFT_DCLICK = None):
        self._canvas.ZoomToBB()

    def on_resize(self, _event: wx.EVT_SIZE):
        print("On Resize called in image panel.")
