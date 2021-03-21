from gui.widgets.panel import Panel
from gui.widgets import fonts

import wx

class CheckBox(wx.CheckBox):
    """A class for a checkbox."""

    def __init__(self, panel: Panel, text: str, size: tuple, position: tuple):
        """Creates a new checkbox."""

        super().__init__(
            panel,
            label = text,
            size = size,
            pos = position
        )

        self.SetFont(fonts.getCalibriFont(9))

    @staticmethod
    def from_attributes(attributes):
        """Creates a new checkbox."""

        new_checkbox = CheckBox(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

        return new_checkbox