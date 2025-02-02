import wx


class DepartmentsPanel(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()
        self.ops = wx.Button(self, label="Ops")
        self.ops.SetFont(font)
        
        self.pods = wx.Button(self, label="PODs")
        self.pods.SetFont(font)
        
        self.quick_start = wx.Button(self, label="Quick Start")
        self.quick_start.SetFont(font)

        self.settings_btn = wx.Button(self, label="Settings")
        self.settings_btn.SetFont(font)

        self.exit_btn = wx.Button(self, label="Exit")
        self.exit_btn.SetFont(font)

        # Sizer layout.
        options_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        options_sizer.Add(
            self.ops, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, 
            border=15
        )

        options_sizer.Add(
            self.pods, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, 
            border=15
        )

        options_sizer.Add(
            self.quick_start, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, 
            border=15
        )

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(options_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(
            self.settings_btn, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, 
            border=15
        )

        sizer.Add(
            self.exit_btn, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, 
            border=15
        )

        self.SetSizer(sizer)
