import fitz
import wx
from src.main.gui import ImageViewer
from src.main.app.interfaces import ImageViewerConfiguration, RootInterface


class ImageViewerController:
    def __init__(
            self, root_application: RootInterface,
            configuration: ImageViewerConfiguration
    ) -> None:
        self._root = root_application
        self._config = configuration
        self._gui = ImageViewer(root_application.frame())
        self._initialise_callbacks()

    def _initialise_callbacks(self) -> None:
        self._gui.bind_exit(self.on_exit)

    def on_exit(self, event = None) -> None:
        self._root.launch_main_menu()

    @property
    def panel(self) -> wx.Panel:
        return self._gui

    def bitmap_movement(self, event: "FloatCanvas.EVT_MOTION") -> None:
        self._gui.status_bar = "%i, %i" % tuple(event.Coords)

    def show(self) -> None:
        self._gui.Show()

    def hide(self) -> None:
        self._gui.Hide()

    def close(self, event: wx.EVT_CLOSE = None) -> None:
        self._gui.close(event)

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

        image = bitmap.ConvertToImage()
        self._gui.set_image(image)