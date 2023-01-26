import wx

class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Departments, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizer()
        #  self.SetBackgroundColour(wx.BLUE)

    def _initialise_buttons(self) -> None:
        self.ops = wx.Button(parent=self, label="Ops")
        self.pods = wx.Button(parent=self, label="PODs")
        self.settings = wx.Button(parent=self, label="Settings")
        self.exit = wx.Button(parent=self, label="Exit")

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        for button in [self.ops, self.pods, self.settings, self.exit]:
            button.SetFont(font)

    def _initialise_sizer(self) -> None:
        flags = wx.ALL|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddStretchSpacer()

        sizer.Add(window=self.ops, proportion=0, flag=flags, border=border)
        sizer.Add(window=self.pods, proportion=0, flag=flags, border=border)

        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.settings, proportion=0, flag=wx.ALL|wx.ALIGN_BOTTOM,
            border=border
        )

        sizer.Add(
            window=self.exit, proportion=0, flag=wx.ALL|wx.ALIGN_BOTTOM,
            border=border
        )

        self.SetSizer(sizer)
