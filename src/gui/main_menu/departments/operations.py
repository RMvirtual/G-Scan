import wx
from .gui import fonts


class Operations(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Operations, self).__init__(parent)

        self.options = OperationsOptions(self)
        self.back = wx.Button(parent=self, label="Back")
        self.back.SetFont(fonts.font(point_size=30, bold=True))

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

        self._initialise_buttons()
        self._initialise_sizers()

    def _initialise_buttons(self) -> None:
        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")

        self.buttons = [self.cust_pwork, self.loading_list]
        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self.buttons:
            button.SetFont(font)

    def _initialise_sizers(self) -> None:
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer.Add(
            window=self.cust_pwork, proportion=0, flag=flags, border=border)

        sizer.Add(
            window=self.loading_list, proportion=0, flag=flags, border=border)

        self.SetSizer(sizer)