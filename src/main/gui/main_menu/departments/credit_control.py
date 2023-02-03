import wx
from src.main.gui import fonts


class CreditControl(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.options = CreditControlOptions(self)
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


class CreditControlOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self._initialise_buttons()
        self._initialise_sizers()

    def _initialise_buttons(self) -> None:
        self.signed_pod = wx.Button(
            parent=self, label="Standard\nDelivery Note")

        self.customer_paperwork_pod = wx.Button(
            parent=self, label="Customer\nPaperwork POD")

        self._buttons = [self.signed_pod, self.customer_paperwork_pod]
        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self._buttons:
            button.SetFont(font)

    def _initialise_sizers(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP

        for button in self._buttons:
            sizer.Add(window=button, proportion=0, flag=flags, border=15)

        self.SetSizer(sizer)