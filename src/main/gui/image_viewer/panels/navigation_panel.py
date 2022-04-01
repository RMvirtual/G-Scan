import wx


class NavigationPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(NavigationPanel, self).__init__(parent=parent)

        self._exit_button = wx.Button(parent=self, label="Exit")

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(
            self._exit_button, 0, wx.ALIGN_CENTRE_HORIZONTAL)

        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)
