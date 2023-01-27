from src.main.gui import ImageViewer
import fitz
import wx

class ImageViewerController:
    def __init__(self, parent_window: wx.Frame):
        self._viewer = ImageViewer(parent_window)

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

        image = bitmap.ConvertToImage()
        self._viewer.set_image(image)

    @property
    def panel(self) -> wx.Panel:
        return self._viewer

    def bitmap_movement(self, event: "FloatCanvas.EVT_MOTION") -> None:
        self._viewer.status_bar = "%i, %i"%tuple(event.Coords)

    def show(self) -> None:
        self._viewer.Show()

    def hide(self) -> None:
        self._viewer.Hide()

    def close(self, event: wx.EVT_CLOSE = None) -> None:
        self._viewer.close(event)

    def bind_exit(self, callback) -> None:
        self._viewer.bind_exit(callback)

    def bind_submit(self, callback) -> None:
        self._viewer.bind_submit(callback)

    def bind_skip(self, callback) -> None:
        self._viewer.bind_skip(callback)

    def bind_split(self, callback) -> None:
        self._viewer.bind_split(callback)

    def bind_bitmap_movement(self, callback) -> None:
        self._viewer.bind_bitmap_movement(callback)