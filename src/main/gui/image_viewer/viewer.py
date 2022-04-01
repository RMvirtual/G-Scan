from src.main.gui.widgets.frame import Frame
from src.main.gui.image_viewer.panels.input_panel import InputPanel
import wx


class ImageViewer(Frame):
    def __init__(self, size):
        super().__init__(size=size, title="Paperwork Viewer")
        self._initialise_widgets()
        self.Show()

    def _initialise_widgets(self) -> None:
        self._input_panel = InputPanel(self)
