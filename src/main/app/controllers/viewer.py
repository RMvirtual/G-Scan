import fitz
import wx
from src.main.app.configurations import ImageViewerConfiguration
from src.main.app.interfaces import RootInterface
from src.main.gui import ImageViewer


class ImageViewerController:
    def __init__(
            self, root_application: RootInterface,
            configuration: ImageViewerConfiguration
    ) -> None:
        self._root = root_application
        self._config = configuration
        self._initialise_gui()
        self._initialise_callbacks()

    def _initialise_gui(self) -> None:
        self._gui = ImageViewer(self._root.window)
        self._root.window.set_panel(self._gui)

    def _initialise_callbacks(self) -> None:
        self._gui.bind_exit(self.on_exit)

    def on_exit(self, event = None) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

    @property
    def panel(self) -> wx.Panel:
        return self._gui

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


