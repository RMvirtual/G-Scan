import wx


class Operations(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Operations, self).__init__(parent)

        self.options = OperationsOptions(self)
        self.back = wx.Button(parent=self, label="Back")
        self.back.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(
            window=self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT,
            border=15
        )

        self.SetSizer(sizer)


class OperationsOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(OperationsOptions, self).__init__(parent)

        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")

        for button in [self.cust_pwork, self.loading_list]:
            button.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer.Add(self.cust_pwork, proportion=0, flag=flags, border=15)
        sizer.Add(self.loading_list, proportion=0, flag=flags, border=15)
        self.SetSizer(sizer)

