import wx


class InputPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._reference_input_label = wx.StaticText(
            parent=self, label="Please enter job reference:")

        self._job_reference_input = wx.TextCtrl(parent=self)
        self._submit_button = wx.Button(parent=self, label="Submit")
        self._skip_button = wx.Button(parent=self, label="Skip")
        self._split_button = wx.Button(parent=self, label="Split")

        sizer = wx.GridBagSizer(vgap=0, hgap=0)
        sizer.Add(self._reference_input_label, pos=(0, 0), span=(1, 4))
        sizer.Add(self._job_reference_input, pos=(1, 0))
        sizer.Add(self._submit_button, pos=(1, 1))
        sizer.Add(self._skip_button, pos=(1, 2))
        sizer.Add(self._split_button, pos=(1, 3))

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)

        self.SetBackgroundColour(colour=wx.YELLOW)