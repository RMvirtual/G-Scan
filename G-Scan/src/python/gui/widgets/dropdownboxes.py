from gui.widgets.panel import Panel
from gui.widgets.widget import Widget

import wx

class DropdownBox(wx.ComboBox, Widget):
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

        super(wx.ComboBox, self).__init__()

        self.SetFont(self.getCalibriFont(9))
        self.SetBackgroundColour("LIGHT GREY")