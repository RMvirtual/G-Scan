from src.main.gui.image_viewer.panels.image_panel import ImagePanel
from src.main.gui.image_viewer.panels.input_panel import InputPanel
from src.main.gui.image_viewer.panels.navigation_panel import NavigationPanel
import wx


class ImageViewer(wx.Frame):
    def __init__(self, size):
        super().__init__(parent=None, size=size, title="Paperwork Viewer")
        self._initialise_widgets()
        self.Show()

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def _initialise_widgets(self) -> None:
        self._input_panel = InputPanel(self)
        self._image_panel = ImagePanel(self)
        self._navigation_panel = NavigationPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Frame is blue colour.
        sizer.Add(self._input_panel, 0, flag=wx.EXPAND)  # Yellow
        sizer.Add(self._image_panel, 1, flag=wx.EXPAND)  # Red
        sizer.Add(self._navigation_panel, 0, flag=wx.EXPAND)  # Green

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.BLUE)

    def set_image(self, image_path: str):
        self._image_panel.set_image(image_path)

    def on_resize(self, event: wx.Event):
        self._image_panel.resize_image()
        event.Skip()
