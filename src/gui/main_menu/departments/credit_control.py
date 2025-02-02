import wx


class CreditControl(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.options = CreditControlOptions(self)
    
        self.back = wx.Button(self, label="Back")
        self.back.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        
        sizer.Add(
            self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)


class CreditControlOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.signed_pod = wx.Button(self, label="Standard\nDelivery Note")

        self.customer_paperwork_pod = wx.Button(
            self, label="Customer\nPaperwork POD")

        buttons = [self.signed_pod, self.customer_paperwork_pod]

        for button in buttons:
            button.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in buttons:
            sizer.Add(
                button, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, 
                border=15
            )

        self.SetSizer(sizer)
