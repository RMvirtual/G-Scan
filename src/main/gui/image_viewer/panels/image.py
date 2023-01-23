import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas
from wx.lib.floatcanvas.FloatCanvas import ScaledBitmap2

class ImagePanel(NavCanvas):
    def __init__(self, parent: wx.Frame):
        super().__init__(
            parent=parent, id=-1, size=wx.DefaultSize, ProjectionFun=None,
            BackgroundColor="wx.LIGHT_GREY", Debug=False
        )

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self.Canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self.Canvas.Bind(wx.EVT_LEFT_DCLICK, self.zoom_to_fit)
        self.Canvas.Bind(wx.EVT_SIZE, self.on_resize)

    def set_image(self, image: wx.Image) -> None:
        scaled_bitmap = ScaledBitmap2(
            image,
            (0, 0),
            Height=image.GetHeight(),
            Position="tl"
        )

        self.Canvas.AddObject(scaled_bitmap)
        self.Canvas.Draw()
        self.Canvas.ZoomToBB()

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self.Canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def zoom_to_fit(self, _event: wx.EVT_LEFT_DCLICK = None):
        self.Canvas.ZoomToBB()

    def on_resize(self, _event: wx.EVT_SIZE):
        print("On Resize called in image panel.")
