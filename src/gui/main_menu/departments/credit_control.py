import wx


class CreditControlPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.standard_btn = wx.Button(self, label="Standard\nDelivery Note")

        self.customer_paperwork_btn = wx.Button(
            self, label="Customer\nPaperwork POD")

        self.back_btn = wx.Button(self, label="Back")

        all_buttons = [
            self.standard_btn, self.customer_paperwork_btn, self.back_btn]
        
        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

        for button in all_buttons:
            button.SetFont(font)

        # Sizer layout.
        docs_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        docs_flag = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP

        docs_sizer.Add(
            self.standard_btn, proportion=0, flag=docs_flag, border=15)

        docs_sizer.Add(
            self.customer_paperwork_btn, proportion=0, flag=docs_flag, 
            border=15
        )

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(docs_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        
        sizer.Add(
            self.back_btn, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)
