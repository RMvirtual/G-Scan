from gui.widgets.panel import Panel
from gui.widgets import fonts

import wx

class Button(wx.Button):
    """A class for a button."""

    def __init__(self, panel: Panel, text: str, size: tuple, position: tuple):
        """Creates a new button."""

        super().__init__(
            panel,
            label = text,
            size = size,
            pos = position
        )

        self.SetFont(fonts.getCalibriFont(11))

    def bindFunctionToClick(self, callbackFunction) -> None:
        """Assigns a callback function to run when the button is
        clicked.
        """

        self.Bind(
            wx.EVT_BUTTON,
            callbackFunction,
            self
        )