import wx
from wx.lib.floatcanvas import FloatCanvas
from src.main.documents import rendering
from src.main.gui.image_viewer.panels.page_view import PageView


class PageViewController:
    def __init__(self, page_canvas: PageView):
        self._panel = page_canvas
        self._canvas = page_canvas.canvas

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self._canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self._canvas.Bind(wx.EVT_LEFT_DCLICK, self.fit_page_to_panel)

    def load_image(self, image: wx.Image) -> None:
        bitmap = FloatCanvas.ScaledBitmap(
            Bitmap=image, XY=(0,0), Height=image.GetHeight(), Position="bl")

        self._canvas.ClearAll()
        self._canvas.AddObject(bitmap)
        self._canvas.ZoomToBB()

    def set_total_pages(self, quantity: int or str) -> None:
        self._panel.set_total_pages(quantity)

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self._canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def fit_page_to_panel(self, _event: wx.EVT_LEFT_DCLICK = None):
        self._canvas.ZoomToBB()