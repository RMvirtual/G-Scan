from gui.widgets.widget import Widget
from gui.widgets.panel import Panel

import wx

class RadioButtonMaster(Widget, wx.RadioButton):
    """A class for a radio button that represents the start of a new
    group of connected radio buttons.
    """

    def __init__(self, panel: Panel, text: str, size: tuple,
            position: tuple) -> None:
        """Creates a new Master Radio Button."""

        super().__init__()

        super(Widget, self).__init__(
            panel,
            label=text,
            size=size,
            pos=position,
            style=wx.RB_GROUP
        )

        self.SetFont(self.getCalibriFont(11))

class RadioButtonSubject(Widget, wx.RadioButton):
    """A class for a radio button that represents the start of a new
    group of connected radio buttons.
    """

    def __init__(self, panel: Panel, text: str, size: tuple,
            position: tuple) -> None:
        """Creates a new Master Radio Button."""

        super().__init__()

        super(Widget, self).__init__(
            panel,
            label=text,
            size=size,
            pos=position,
        )

        self.SetFont(self.getCalibriFont(11))
