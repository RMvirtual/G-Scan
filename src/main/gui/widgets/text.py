import gui.widgets.fonts as fonts
from gui.widgets.widget import Attributes
from wx import BORDER_NONE, BORDER_SIMPLE, TE_MULTILINE, TE_READONLY, \
    TextCtrl, StaticText

class TextEntryBox(TextCtrl):
    """A class for a text entry box."""

    def __init__(self, panel, text, size, position):
        """Creates a new text entry box."""

        super().__init__(
            panel,
            value=text,
            size=size,
            pos=position,
            style=BORDER_SIMPLE
        )

        self.SetFont(fonts.getCalibriFont(14))
        self.SetBackgroundColour("LIGHT GREY")
        # self.SetMaxLength(11)

    @staticmethod
    def from_attributes(attributes: Attributes):
        """Creates a new text label box from attributes."""

        return TextEntryBox(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

    def get_value(self) -> str:
        """Returns the value found in the text box."""
        
        return self.GetValue()

    def clear_value(self) -> None:
        """Clears the text in the text box."""

        self.Clear()

class TextLabel(StaticText):
    """A class for a text label box for instructions etc."""

    def __init__(self, panel, text, size, position):
        """Creates a new text label box."""

        super().__init__(
            panel,
            label=text,
            pos=position,
            size=size,
            style=BORDER_NONE
        )

        self.SetFont(fonts.getCalibriFont(14))

    @staticmethod
    def from_attributes(attributes: Attributes):
        """Creates a new text label box from attributes."""

        return TextLabel(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

class TextConsole(TextCtrl):
    """A class for a text console."""

    def __init__(self, panel, size, position):
        super().__init__(
            panel,
            value="",
            size=size,
            pos=position,
            style=TE_MULTILINE | TE_READONLY | BORDER_SIMPLE
        )

        self.SetFont(fonts.getCalibriFont(14))
        self.SetBackgroundColour("LIGHT GREY")

        self.SetEditable(False)

    @staticmethod
    def from_attributes(attributes: Attributes):
        """Creates a new text label box from attributes."""

        return TextConsole(
            attributes.parent_widget,
            attributes.size, attributes.position
        )

    def write(self, text: str):
        """Writes to the console."""

        self.WriteText(text)