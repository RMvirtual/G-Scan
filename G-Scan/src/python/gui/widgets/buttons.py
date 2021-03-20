from gui.widgets.panel import Panel
from gui.widgets import fonts
from gui.widgets.widgetattributes import WidgetAttributes

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

    @staticmethod
    def fromAttributes(attributes:WidgetAttributes):
        """Creates a new button."""

        new_button = Button(
            attributes.parent_widget, attributes.text, attributes.size,
            attributes.position)

        if attributes.callback_function:
            new_button.bindFunctionToClick(attributes.callback_function)

        return new_button