import wx


class UserToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self._initialise()

    def _initialise(self) -> None:
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self._input_label = wx.StaticText(
            self, label="Please enter job reference:")

        self.input = wx.TextCtrl(self)
        self.submit = wx.Button(self, label="Submit")
        self.skip = wx.Button(self, label="Skip")
        self.split = wx.Button(self, label="Split")

    def _initialise_sizer(self) -> None:
        border = 5
        sizer = wx.GridBagSizer(vgap=0, hgap=0)

        sizer.Add(
            window=self._input_label, pos=(0,0), span=(1,4),
            flag=wx.ALL, border=border
        )

        sizer.Add(window=self.input, pos=(1,0), flag=wx.ALL, border=border)
        sizer.Add(window=self.submit, pos=(1,1), flag=wx.ALL, border=border)
        sizer.Add(window=self.skip, pos=(1,2), flag=wx.ALL, border=border)
        sizer.Add(window=self.split, pos=(1,3), flag=wx.ALL, border=border)

        self.SetSizer(sizer)

    def clear_job_ref_input(self) -> None:
        self.input.Clear()

    def job_ref_input(self) -> str:
        return self.input.GetValue()
