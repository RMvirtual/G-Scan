import wx
from wx.lib.floatcanvas import FloatCanvas
from src.main.app.interfaces import RootInterface
from src.main.documents import rendering
from src.main.gui.image_viewer.panels.page_canvas import PageCanvas


class PageCanvasController:
    def __init__(
            self, root_application: RootInterface, page_canvas: PageCanvas):
        self._root = root_application
        self._canvas_panel = page_canvas
        self._canvas = page_canvas.canvas

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self._canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self._canvas.Bind(wx.EVT_LEFT_DCLICK, self.fit_page_to_panel)

    def load_file(self, image_path: str) -> None:
        image = rendering.render(image_path)
        self.load_image(image)

    def load_image(self, image: wx.Image) -> None:
        bitmap = FloatCanvas.ScaledBitmap(
            Bitmap=image, XY=(0,0), Height=image.GetHeight(), Position="bl")

        self._canvas.AddObject(bitmap)
        self._canvas.ZoomToBB()

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self._canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def fit_page_to_panel(self, _event: wx.EVT_LEFT_DCLICK = None):
        self._canvas.ZoomToBB()