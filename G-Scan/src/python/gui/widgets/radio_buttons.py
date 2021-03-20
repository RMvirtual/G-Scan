from gui.widgets import fonts
from gui.widgets.panel import Panel

import wx

class RadioButtonMaster(wx.RadioButton):
    """A class for a radio button that represents the start of a new
    group of connected radio buttons.
    """

    def __init__(self, panel: Panel, text: str, size: tuple,
            position: tuple) -> None:
        """Creates a new Master Radio Button."""

        super().__init__(
            panel,
            label=text,
            size=size,
            pos=position,
            style=wx.RB_GROUP
        )

        self.SetFont(fonts.getCalibriFont(11))

class RadioButtonSubject(wx.RadioButton):
    """A class for a radio button that represents the start of a new
    group of connected radio buttons.
    """

    def __init__(self, panel: Panel, text: str, size: tuple,
            position: tuple) -> None:
        """Creates a new Master Radio Button."""

        super().__init__(
            panel,
            label=text,
            size=size,
            pos=position,
        )

        self.SetFont(fonts.getCalibriFont(11))