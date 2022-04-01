from src.main.gui.widgets.frame import Frame


class ImageViewer(Frame):
    def __init__(self, size):
        super().__init__(size=size, title="Paperwork Viewer")
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self.SetBackgroundColour("WHITE")

