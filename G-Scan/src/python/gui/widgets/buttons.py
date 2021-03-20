from gui.widgets.panel import Panel
from gui.widgets.widget import Widget

import wx

class Button(wx.Button, Widget):
    """A class for a button."""

    def __init__(self, panel: Panel, text: str, size: tuple, position: tuple):
        """Creates a new button."""

        super().__init__(
            panel,
            label = text,
            size = size,
            pos = position
        )

        self.SetFont(self.getCalibriFont(11))

    def bindFunctionToClick(self, callbackFunction) -> None:
        """Assigns a callback function to run when the button is
        clicked.
        """

        self.Bind(
            wx.EVT_BUTTON,
            callbackFunction,
            self
        )