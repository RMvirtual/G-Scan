from src.main.gui.image_viewer.viewer import ImageViewer
import fitz
import wx


class ImageViewerController:
    def __init__(self):
        self._initialise_viewer()

    def _initialise_viewer(self):
        self._viewer = ImageViewer()
        self._initialise_event_callbacks()

    def _initialise_event_callbacks(self) -> None:
        self._viewer.set_exit_callback(self.close)
        self._viewer.set_submit_callback(self.submit)
        self._viewer.set_skip_callback(self.skip)
        self._viewer.set_split_callback(self.split)

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height,
            pixel_buffer.samples
        )

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
