from wx.core import wxEVT_RADIOBUTTON
import src.main.gui.widgets.fonts as fonts
from src.main.gui.widgets.panel import Panel
from wx import RadioButton, RB_GROUP

class RadioButtonMaster(RadioButton):
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
            style=RB_GROUP
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

    def bind_event_handler(self, event_handler):
        self.Bind(wxEVT_RADIOBUTTON, event_handler)

class RadioButtonSubject(RadioButton):
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

    def bind_event_handler(self, event_handler):
        self.Bind(wxEVT_RADIOBUTTON, event_handler)
