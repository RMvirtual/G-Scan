from wx.core import Font
from gui.widgets.panel import Panel
from gui.widgets.fonts import *

import wx

class DropdownBox(wx.ComboBox):
    """A class for a dropdown box."""

    def __init__(self, panel: Panel, starting_value: str, size: tuple,
            position: tuple, options: tuple):
        """Creates a new dropdown box."""

        super().__init__(
            panel,
            value=starting_value,
            size=size,
            pos=position,
            choices=options,
            style=wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.SetFont(getCalibriFont(9))
        self.SetBackgroundColour("LIGHT GREY")

    @staticmethod
    def from_attributes(attributes):
        """Creates a new dropdown box."""

        new_dropdown_box = DropdownBox(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position, attributes.options
        )

        return new_dropdown_box