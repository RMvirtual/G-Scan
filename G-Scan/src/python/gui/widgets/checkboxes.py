from gui.widgets.panel import Panel
from gui.widgets.widget import Widget

import wx

class CheckBox(wx.CheckBox, Widget):
    """A class for a checkbox."""

    def __init__(self, panel: Panel, text: str, size: tuple, position: tuple):
        """Creates a new checkbox."""

        super().__init__(
            panel,
            label = text,
            size = size,
            pos = position
        )

        super(wx.CheckBox, self).__init__()

        self.SetFont(self.getCalibriFont(9))