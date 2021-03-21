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

    @staticmethod
    def from_attributes(attributes):
        """Creates a new master radio button."""

        new_radio_button = RadioButtonMaster(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

        return new_radio_button

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

    @staticmethod
    def from_attributes(attributes):
        """Creates a new master radio button."""

        new_radio_button = RadioButtonSubject(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

        return new_radio_button
