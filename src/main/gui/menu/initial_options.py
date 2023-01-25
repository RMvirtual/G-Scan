import wx

class InitialOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(InitialOptions, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizer()
        self.SetBackgroundColour(wx.BLUE)

    def _initialise_buttons(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        self.ops = wx.Button(parent=self, label="Ops")
        self.ops.SetFont(font)

        self.pods = wx.Button(parent=self, label="PODs")
        self.pods.SetFont(font)

    def _initialise_sizer(self) -> None:
        flags = wx.ALL|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddStretchSpacer()

        sizer.Add(window=self.ops, proportion=0, flag=flags, border=border)
        sizer.Add(window=self.pods, proportion=0, flag=flags, border=border)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)
