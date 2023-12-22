import wx

from gui.metrics import recommended_metrics


class Window(wx.Frame):
    def __init__(self):
        size, position = recommended_metrics()
        super().__init__(None, title="", size=size, pos=position)

        self._panel = None
        self.SetBackgroundColour(colour=wx.WHITE)

    def set_panel(self, panel: wx.Panel) -> None:
        if self._panel:
            self.GetSizer().Replace(self._panel, panel)
            self._panel = panel

        else:
            self._panel = panel

            sizer = wx.BoxSizer(orient=wx.VERTICAL)
            sizer.Add(window=self._panel, proportion=1, flag=wx.EXPAND)

            self.SetSizer(sizer)
            self.Layout()

        self.Layout()
