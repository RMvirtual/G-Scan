import fitz
import wx
from src.main.gui import ImageViewer
from src.main.app.root.interface import RootInterface


class ImageViewerController:
    def __init__(self, root_application: RootInterface) -> None:
        self._root = root_application
        self._gui = ImageViewer(root_application.frame())
        self._initialise_callbacks()

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

        image = bitmap.ConvertToImage()
        self._gui.set_image(image)

    def _initialise_callbacks(self) -> None:
        self.bind_exit(self.on_exit)

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

    def bind_exit(self, callback) -> None:
        self._gui.bind_exit(callback)

    def bind_submit(self, callback) -> None:
        self._gui.bind_submit(callback)

    def bind_skip(self, callback) -> None:
        self._gui.bind_skip(callback)

    def bind_split(self, callback) -> None:
        self._gui.bind_split(callback)

    def bind_bitmap_movement(self, callback) -> None:
        self._gui.bind_bitmap_movement(callback)