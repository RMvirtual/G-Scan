import wx


# TODO: Mostly duplicated by the CreditControlPanel.

class OperationsPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")
        self.back = wx.Button(parent=self, label="Back")
        
        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

        for button in [self.cust_pwork, self.loading_list, self.back]:
            button.SetFont(font)

        # Sizer layout.
        doc_types_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        doc_types_sizer.Add(self.cust_pwork, proportion=0, flag=flags, border=15)
        doc_types_sizer.Add(self.loading_list, proportion=0, flag=flags, border=15)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(
            doc_types_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        
        sizer.Add(
            window=self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT,
            border=15
        )

        self.SetSizer(sizer)
