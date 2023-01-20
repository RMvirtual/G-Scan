import wx
from wx.lib.floatcanvas.FCObjects import ScaledBitmap
from wx.lib.floatcanvas.FloatCanvas import FloatCanvas


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        width, height = self.GetSize()
        self._canvas = FloatCanvas(self, size=(width, height))
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.RED)
        self._canvas.SetBackgroundColour(wx.LIGHT_GREY)
        self._initialise_bindings()

    def _initialise_sizer(self) -> None:
        self._sizer = wx.BoxSizer(wx.VERTICAL)

        self._sizer.Add(
            window=self._canvas,
            flag=wx.ALIGN_TOP | wx.ALIGN_LEFT |
            wx.SHAPED | wx.EXPAND
        )

        self.SetSizer(self._sizer)
        self._sizer.Size

    def _initialise_bindings(self) -> None:
        self._canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self._canvas.Bind(wx.EVT_LEFT_DCLICK, self.zoom_to_fit)
        self._canvas.Bind(wx.EVT_SIZE, self.on_resize)

    def set_image(self, image: wx.Image) -> None:
        width, height = self.GetSize()
        scaled_bitmap = ScaledBitmap(image.ConvertToBitmap(), (0, 0), height)
        self._canvas.AddObject(scaled_bitmap)
        self._canvas.Draw()

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self._canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def zoom_to_fit(self, _event: wx.EVT_LEFT_DCLICK):
        self._canvas.ZoomToBB()

    def on_resize(self, _event: wx.EVT_SIZE):
        print("On Resize called in image panel.")

    @property
    def size(self) -> tuple[int, int]:
        """Tuple of size in pixels (x, y)."""
        return self.GetSize()
