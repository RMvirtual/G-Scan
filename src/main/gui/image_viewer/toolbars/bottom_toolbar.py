import wx


class BottomToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(BottomToolbar, self).__init__(
            parent=parent
        )
        self.exit = wx.Button(parent=self, label="Exit")
        self._initialise_sizer()

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=5
        )

        self.SetSizer(sizer)