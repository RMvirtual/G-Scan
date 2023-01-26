import wx


class Operations(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Operations, self).__init__(parent)

        self.options = OperationsOptions(self)
        self.back = wx.Button(parent=self, label="Back")
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())
        self.back.SetFont(font)

        border = 15
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1,
            flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=border
        )

        sizer.Add(
            window=self.back, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=border)

        self.SetSizer(sizer)


class OperationsOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(OperationsOptions, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizers()

    def _initialise_buttons(self) -> None:
        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        for button in [self.cust_pwork, self.loading_list]:
            button.SetFont(font)

    def _initialise_sizers(self) -> None:
        flags = wx.ALL|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.cust_pwork, proportion=0, flag=flags, border=border)

        sizer.Add(
            window=self.loading_list, proportion=0, flag=flags, border=border)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)