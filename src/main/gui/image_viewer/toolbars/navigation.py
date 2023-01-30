import wx


class NavigationPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(NavigationPanel, self).__init__(
            parent=parent
        )
        self.SetBackgroundColour(colour=wx.GREEN)
        self.exit = wx.Button(parent=self, label="Exit")
        self._initialise_sizer()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=5
        )

        self.SetSizer(sizer)