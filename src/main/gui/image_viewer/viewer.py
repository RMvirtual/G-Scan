import wx
from wx.lib.floatcanvas import FloatCanvas
from src.main.gui.image_viewer.panels.bitmap_canvas import BitmapViewer
from src.main.gui.image_viewer.toolbars.input import InputPanel
from src.main.gui.image_viewer.toolbars.navigation import NavigationPanel
from src.main.gui.image_viewer.panels.files import FilesPanel
from src.main.gui.image_viewer.toolbars.menu_bar import MenuBar


class ImageViewer(wx.Panel):
    def __init__(self, parent_window: wx.Frame):
        super().__init__(parent=parent_window)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._initialise_panels()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

    def _initialise_panels(self) -> None:
        self.menu_bar = MenuBar()
        self.Parent.SetMenuBar(self.menu_bar)

        self.input_bar = InputPanel(self)
        self.bitmap_viewer = BitmapViewer(self)
        self.files = FilesPanel(self)
        self.bottom_toolbar = NavigationPanel(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self.input_bar, proportion=0, flag=wx.EXPAND)
        sizer.Add(sizer=self._bitmap_sizer(), proportion=1, flag=wx.EXPAND)
        sizer.Add(window=self.bottom_toolbar, proportion=0, flag=wx.EXPAND)

        self.SetSizer(sizer)

    def _bitmap_sizer(self) -> wx.Sizer:
        result = wx.BoxSizer(orient=wx.HORIZONTAL)
        result.Add(window=self.bitmap_viewer, proportion=3, flag=wx.EXPAND)
        result.Add(window=self.files, proportion=1, flag=wx.EXPAND)

        return result

    def set_image(self, image: wx.Image) -> None:
        self.bitmap_viewer.load_image(image)

