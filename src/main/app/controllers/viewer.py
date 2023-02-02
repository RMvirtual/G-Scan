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
        self._bind_callbacks()



        if self._root.window.IsFrozen():
            self._root.window.Thaw()

    def _initialise_gui(self) -> None:
        self._gui = ImageViewer(self._root.window)
        self._root.window.set_panel(self._gui)

    def _bind_callbacks(self) -> None:
        self._gui.bottom_toolbar.exit.Bind(wx.EVT_BUTTON, self.on_exit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._root.window.Bind(
            wx.EVT_MENU, self.on_menu_bar, self._gui.file_menu.quit)

    def on_menu_bar(self, event: wx.EVT_MENU = None) -> None:
        print("In onMenuBar")
        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event = None) -> None:
        self._tear_down_gui()

    def _tear_down_gui(self) -> None:
        self._root.window.Freeze()
        self._gui.Destroy()
        self._root.window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

    def load(self, image_path: str) -> None:
        document = fitz.open(image_path)
        _number_of_pages = document.page_count
        page = document[0]
        pixel_buffer = page.get_pixmap()

        bitmap = wx.Bitmap.FromBuffer(
            pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

        image = bitmap.ConvertToImage()
        self._gui.set_image(image)
