import wx


class InputPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._reference_input_label = wx.StaticText(
            parent=self, label="Please enter job reference:")

        self._job_reference_input = wx.TextCtrl(parent=self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._reference_input_label, 0, wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self._job_reference_input, 0, wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)
