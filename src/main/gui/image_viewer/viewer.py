from wx import Frame as wxFrame


class ImageViewer(wxFrame):
    def __init__(self, size):
        super().__init__(None, size=size, title="Paperwork Viewer")
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self.SetBackgroundColour("WHITE")


