import wx

class Frame(wx.Frame):
    """A class for a frame window."""

    def __init__(self, size, title):
        """Creates a new frame."""
       
        super().__init__(
            None,
            size=size,
            title=title
        )

        self.SetBackgroundColour("WHITE")