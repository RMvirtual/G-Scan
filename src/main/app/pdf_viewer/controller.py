from src.main.gui.image_viewer.viewer import ImageViewer
import fitz
import wx

class ImageViewerController:
    def __init__(self):
        self._initialise_viewer()

    def _initialise_viewer(self):
        self._viewer = ImageViewer("G-Scan")
        self._bind_event_callbacks()
        self._viewer.Show()

    def _bind_event_callbacks(self) -> None:
        self._viewer.bind_exit(self.close)
        self._viewer.bind_submit(self.submit)
        self._viewer.bind_skip(self.skip)
        self._viewer.bind_split(self.split)
        self._viewer.bind_bitmap_movement(self.bitmap_movement)

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

        image = bitmap.ConvertToImage()
        self._viewer.set_image(image)

    def close(self, event: wx.EVT_CLOSE = None) -> None:
        self._viewer.close(event)

    def submit(self, event: any = None) -> None:
        print("SUBMIT")

    def skip(self, event: any = None) -> None:
        print("SKIP")

    def split(self, event: any = None) -> None:
        print("SPLIT")

    def bitmap_movement(self, event: "FloatCanvas.EVT_MOTION") -> None:
        self._viewer.status_bar = "%i, %i"%tuple(event.Coords)
