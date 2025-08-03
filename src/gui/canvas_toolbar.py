import wx


class CanvasToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.camera_lbl = wx.StaticText(self, label="Camera")

        sizer = wx.BoxSizer()
        sizer.Add(self.camera_lbl)

        self.SetSizerAndFit(sizer)
