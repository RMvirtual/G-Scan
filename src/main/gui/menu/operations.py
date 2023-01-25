import wx


class OperationsOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(OperationsOptions, self).__init__(parent)

        self._initialise_buttons()

    def _initialise_buttons(self) -> None:
        font = wx.Font(wx.FontInfo(pointSize=30).Bold())

        self.loading_list = wx.Button(parent=self, label="Loading\nList")
        self.loading_list.SetFont(font)

        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.cust_pwork.SetFont(font)

    def _initialise_sizers(self) -> None:
        flags = wx.ALL|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        sizer.AddStretchSpacer()

        sizer.Add(
            window=self.loading_list, proportion=0, flag=flags, border=border)

        sizer.Add(
            window=self.cust_pwork, proportion=0, flag=flags, border=border)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)