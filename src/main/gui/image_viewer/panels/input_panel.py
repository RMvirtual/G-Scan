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

        sizer = wx.FlexGridSizer(rows=1, cols=5, vgap=0, hgap=5)
        sizer.Add(self._reference_input_label)
        sizer.Add(self._job_reference_input)
        sizer.Add(self._submit_button)
        sizer.Add(self._skip_button)
        sizer.Add(self._split_button)

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)
