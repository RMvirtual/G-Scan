import wx


class CanvasToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.camera_lbl = wx.StaticText(self, label="Camera")

        self.camera_x_lbl = wx.StaticText(
            self, label="X", style=wx.ALIGN_CENTER_HORIZONTAL
        )

        self.camera_x_entry = wx.TextCtrl(self, value="0.0")

        self.camera_y_lbl = wx.StaticText(
            self, label="Y", style=wx.ALIGN_CENTER_HORIZONTAL
        )

        self.camera_y_entry = wx.TextCtrl(self, value="0.0")

        sizer = wx.BoxSizer()
        label_pad = wx.ALIGN_CENTRE_VERTICAL | wx.RIGHT
        border = 5

        sizer.Add(self.camera_lbl, 0, label_pad, border)
        sizer.Add(self.camera_x_lbl, 0, label_pad, border)
        sizer.Add(self.camera_x_entry, 0, wx.RIGHT, border)
        sizer.Add(self.camera_y_lbl, 0, label_pad, border)
        sizer.Add(self.camera_y_entry, 0, wx.RIGHT, border)

        self.SetSizerAndFit(sizer)
