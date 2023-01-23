import wx


class InputPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._create_widgets()
        self._layout_widgets()
        self.SetBackgroundColour(colour=wx.YELLOW)

    def _create_widgets(self) -> None:
        self._reference_input_label = wx.StaticText(
            self, label="Please enter job reference:")

        self._job_ref_input = wx.TextCtrl(self)
        self._submit_button = wx.Button(self, label="Submit")
        self._skip_button = wx.Button(self, label="Skip")
        self._split_button = wx.Button(self, label="Split")

    def _layout_widgets(self) -> None:
        sizer = wx.GridBagSizer(vgap=0, hgap=0)
        sizer.Add(self._reference_input_label, pos=(0, 0), span=(1, 4))
        sizer.Add(self._job_ref_input, pos=(1, 0))
        sizer.Add(self._submit_button, pos=(1, 1))
        sizer.Add(self._skip_button, pos=(1, 2))
        sizer.Add(self._split_button, pos=(1, 3))

        sizer.SetSizeHints(self)
        self.SetSizer(sizer)

    def bind_submit_callback(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._submit_button)

    def bind_skip_callback(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._skip_button)

    def bind_split_callback(self, callback) -> None:
        self.Bind(wx.EVT_BUTTON, callback, self._split_button)

    def clear_job_ref_input(self) -> None:
        self._job_ref_input.Clear()

    def job_ref_input(self) -> str:
        return self._job_ref_input.GetValue()
