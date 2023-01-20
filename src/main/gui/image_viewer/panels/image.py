import wx
from wx.lib.floatcanvas.FCObjects import ScaledBitmap
from wx.lib.floatcanvas.FloatCanvas import FloatCanvas


class ImagePanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(ImagePanel, self).__init__(parent=parent)

        width, height = self.GetSize()
        self._nav_canvas = FloatCanvas(self, size=(width, height))
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.RED)
        self._nav_canvas.SetBackgroundColour("Grey")
        self._initialise_navigation()

    def _initialise_sizer(self) -> None:
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(
            self._nav_canvas, 0,
            wx.ALIGN_TOP | wx.ALIGN_LEFT |
            wx.SHAPED | wx.RESERVE_SPACE_EVEN_IF_HIDDEN
        )
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)

    def _initialise_navigation(self) -> None:
        self._nav_canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self._nav_canvas.Bind(wx.EVT_LEFT_DCLICK, self.zoom_to_fit)

    def set_image(self, image: wx.Image) -> None:
        width, height = self.GetSize()

        self._nav_canvas.AddScaledBitmap(image, (0, 0), height, "cc")
        self._nav_canvas.Draw()

    def set_bitmap(self, bitmap: wx.Bitmap) -> None:
        pass

    def on_wheel(self, event):
        self._nav_canvas.Zoom(
            1 / 1.2 if event.GetWheelRotation() < 0 else 1.2,
            event.Position, "Pixel", keepPointInPlace=True)

    def zoom_to_fit(self, _event):
        self._nav_canvas.ZoomToBB()

    @property
    def size(self) -> tuple[int, int]:
        """Tuple of size in pixels (x, y)."""
        return self.GetSize()
