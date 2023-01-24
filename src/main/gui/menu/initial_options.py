import wx

class InitialOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(InitialOptions, self).__init__(parent)

        self.ops = wx.Button(parent=self, label="Ops")
        self.pods = wx.Button(parent=self, label="PODs")

        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizer.AddStretchSpacer(prop=1)

        self.sizer.Add(
            window=self.ops, proportion=0,
            flag=wx.ALL|wx.ALIGN_CENTRE_VERTICAL, border=10
        )

        self.sizer.Add(
            window=self.pods, proportion=0,
            flag=wx.ALL|wx.ALIGN_CENTRE_VERTICAL, border=10
        )

        self.sizer.AddStretchSpacer(prop=1)

        self.SetSizer(self.sizer)
        self.SetBackgroundColour(wx.BLUE)