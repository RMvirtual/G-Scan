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