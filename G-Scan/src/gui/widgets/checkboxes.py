from gui.widgets.panel import Panel
import gui.widgets.fonts as fonts
from gui.widgets.widget import Attributes
from wx import CheckBox as wxCheckBox

class CheckBox(wxCheckBox):
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
    def from_attributes(attributes: Attributes):
        """Creates a new checkbox."""

        new_checkbox = CheckBox(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

        return new_checkbox