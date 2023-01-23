import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas
from wx.lib.floatcanvas import FloatCanvas

class BitmapViewer(NavCanvas):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(
            parent=parent,
            ProjectionFun=None,
            BackgroundColor="DARK SLATE BLUE"
        )

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self.Canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self.Canvas.Bind(wx.EVT_LEFT_DCLICK, self.zoom_to_fit)

    def load_image(self, image: wx.Image) -> None:
        scaled_bitmap = FloatCanvas.ScaledBitmap2(
            image, (0, 0), Height=image.GetHeight(), Position="tl")

        self.Canvas.AddObject(scaled_bitmap)
        self.Canvas.ZoomToBB()

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self.Canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def zoom_to_fit(self, _event: wx.EVT_LEFT_DCLICK = None):
        self.Canvas.ZoomToBB()
