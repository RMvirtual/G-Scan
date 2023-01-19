import wx


class NavigationPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(NavigationPanel, self).__init__(parent=parent)
        self.SetBackgroundColour(colour=wx.GREEN)
        self._exit_button = wx.Button(parent=self, label="Exit")
        self._initialise_sizer()

    def _initialise_sizer(self) -> None:
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(self._exit_button, 0, wx.ALIGN_RIGHT)
        self._sizer.SetSizeHints(self)
        self.SetSizer(self._sizer)

    def set_exit_callback(self, callback):
        self.Bind(wx.EVT_BUTTON, callback, self._exit_button)
