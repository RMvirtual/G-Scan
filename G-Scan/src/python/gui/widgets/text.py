from gui.widgets.widget import Widget

import wx

class TextEntryBox(wx.TextCtrl, Widget):
    """A class for a text entry box."""

    def __init__(self, panel, text, size, position):
        """Creates a new text entry box."""

        super().__init__(
            panel,
            value=text,
            size=size,
            pos=position,
            style=wx.BORDER_SIMPLE
        )

        self.SetFont(self.getCalibriFont(14))
        self.SetBackgroundColour("LIGHT GREY")
        self.SetMaxLength(11)

class TextLabel(wx.StaticText, Widget):
    """A class for a text label box for instructions etc."""

    def __init__(self, panel, text, size, position):
        """Creates a new text label box."""

        super().__init__(
            panel,
            label=text,
            pos=position,
            size=size,
            style=wx.BORDER_NONE
        )

        self.SetFont(self.getCalibriFont(14))

class TextConsole(TextEntryBox):
    """A class for a text console."""

    def __init__(self, panel, size, position):
        super().__init__(panel, "", size, position)

        self.SetWindowStyle(
            wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE)

        self.SetEditable(False)