import wx

class TextEntryBox(wx.TextCtrl):
    """A class for a text entry box."""

    def __init__(self, panel, text, size, position):
        """Creates a new text entry box."""

        super().__init__(
            panel,
            value = text,
            size = size,
            pos = position,
            style = wx.BORDER_SIMPLE
        )

        self.SetFont(panel.get_body_font())
        self.SetBackgroundColour("LIGHT GREY")
        self.SetMaxLength(11)

class TextLabel(wx.StaticText):
    """A class for a text label box for instructions etc."""

    def __init__(self, panel, text, size, position):
        """Creates a new text label box."""

        super().__init__(
            panel,
            label = text,
            pos = position,
            size = size,
            style = wx.BORDER_NONE
        )

        self.SetFont(panel.get_body_font())
