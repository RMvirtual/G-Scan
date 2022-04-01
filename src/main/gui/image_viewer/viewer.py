from src.main.gui.widgets.frame import Frame
from src.main.gui.image_viewer.panels.image_panel import ImagePanel
from src.main.gui.image_viewer.panels.input_panel import InputPanel
from src.main.gui.image_viewer.panels.navigation_panel import NavigationPanel
import wx


class ImageViewer(Frame):
    def __init__(self, size):
        super().__init__(size=size, title="Paperwork Viewer")
        self._initialise_widgets()
        self.Show()

    def _initialise_widgets(self) -> None:
        self._input_panel = InputPanel(self)
        self._image_panel = ImagePanel(self)
        self._navigation_panel = NavigationPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._input_panel, 0, wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self._image_panel, 0, wx.EXPAND)
        sizer.Add(self._navigation_panel, 0, wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)

    def set_image(self, image_path: str):
        self._image_panel.setImage(image_path)

