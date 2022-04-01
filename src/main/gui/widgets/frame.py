from wx import Frame as wxFrame


class Frame(wxFrame):
    """A class for a frame window."""

    def __init__(self, size, title):
        """Creates a new frame."""

        super().__init__(
            None,
            size=size,
            title=title
        )

        self.SetBackgroundColour("WHITE")
