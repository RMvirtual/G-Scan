import wx

class InitialOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(InitialOptions, self).__init__(parent)

        font = wx.Font(wx.FontInfo(pointSize=30).Bold())
        self.ops = wx.Button(parent=self, label="Ops")
        self.ops.SetFont(font)

        self.pods = wx.Button(parent=self, label="PODs")
        self.pods.SetFont(font)

        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.sizer.AddStretchSpacer(prop=1)

        self.sizer.Add(
            window=self.ops, proportion=0, flag=wx.ALL|wx.ALIGN_TOP, border=15)

        self.sizer.Add(
            window=self.pods, proportion=0,
            flag=wx.ALL|wx.ALIGN_TOP, border=15
        )

        self.sizer.AddStretchSpacer(prop=1)

        self.SetSizer(self.sizer)
        self.SetBackgroundColour(wx.BLUE)