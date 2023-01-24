import wx
from wx.lib.floatcanvas import FloatCanvas
from src.main.gui.app import screen_size
from src.main.gui.image_viewer.bitmap_canvas import BitmapViewer
from src.main.gui.image_viewer.input import InputPanel
from src.main.gui.image_viewer.navigation import NavigationPanel
from src.main.gui.image_viewer.menu_bar import MenuBar

class ImageViewer(wx.Frame):
    def __init__(self, title: str):
        size, position = screen_size.recommended_metrics()
        super().__init__(parent=None, title=title, size=size, pos=position)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._initialise_status_bar()
        self._initialise_menu_bar()
        self._initialise_panels()
        self._initialise_sizer()

        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

    def _initialise_status_bar(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("HELLO WORLD")

    def _initialise_menu_bar(self) -> None:
        self._menu_bar = MenuBar()
        file_menu = wx.Menu()
        file_item = file_menu.Append(wx.ID_EXIT, "Quit", "Quit application")
        self._menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(self._menu_bar)
        self.Bind(wx.EVT_MENU, self.close, file_item)

    def _initialise_panels(self) -> None:
        self._top_toolbar = InputPanel(self)
        self._bitmap_viewer = BitmapViewer(self)
        self._bottom_toolbar = NavigationPanel(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(window=self._top_toolbar, proportion=0, flag=wx.EXPAND)
        sizer.Add(window=self._bitmap_viewer, proportion=1, flag=wx.EXPAND)
        sizer.Add(window=self._bottom_toolbar, proportion=0, flag=wx.EXPAND)
        self.SetSizer(sizer)

    def close(self, _event: wx.Event = None) -> None:
        self.Close()

    def set_image(self, image: wx.Image) -> None:
        self._bitmap_viewer.load_image(image)

    def bind_exit(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._bottom_toolbar.exit)

    def bind_bitmap_movement(self, callback):
        self._bitmap_viewer.Canvas.Bind(FloatCanvas.EVT_MOTION, callback)

    def bind_submit(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._top_toolbar.submit)

    def bind_skip(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._top_toolbar.skip)

    def bind_split(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._top_toolbar.split)

    @property
    def status_bar(self) -> str:
        return self.GetStatusText()

    @status_bar.setter
    def status_bar(self, new_status: str) -> None:
        self.SetStatusText(new_status)
