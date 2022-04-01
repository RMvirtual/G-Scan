from wx.core import Font
from src.main.gui.widgets.panel import Panel
import src.main.gui.widgets.fonts as fonts
from src.main.gui.widgets.widget import Attributes
from wx import CB_DROPDOWN, CB_READONLY, ComboBox as wxComboBox

class DropdownBox(wxComboBox):
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
            style=CB_DROPDOWN | CB_READONLY
        )

        self.SetFont(fonts.getCalibriFont(9))
        self.SetBackgroundColour("LIGHT GREY")

    @staticmethod
    def from_attributes(attributes: Attributes):
        """Creates a new dropdown box."""

        new_dropdown_box = DropdownBox(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position, attributes.options
        )

        return new_dropdown_box