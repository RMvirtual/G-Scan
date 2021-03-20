import wx

from gui.widgets.widget import Widget

class Panel(wx.Panel, Widget):
    """A basic GUI panel (to be extended further into more concrete
    panels).
    """

    def __init__(self, frame: wx.Frame, size: tuple, position: tuple) -> None:
        """Creates a new panel and attaches it to a frame."""

        super().__init__(
            frame,
            size = size,
            pos = position
        )

        self.__frame = frame