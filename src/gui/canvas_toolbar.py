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

        self.camera_zoom_lbl = wx.StaticText(self, label="Zoom")
        zoom_options = [10, 25, 33, 50, 66, 75, 100, 125, 150, 200, 300, 500]

        self.camera_zoom_combobox = wx.ComboBox(
            self,
            value="100%",
            choices=[f"{level}%" for level in zoom_options],
            style=wx.CB_READONLY,
        )

        sizer = wx.BoxSizer()
        label_style = wx.ALIGN_CENTRE_VERTICAL | wx.RIGHT
        border = 5

        sizer.Add(self.camera_lbl, 0, label_style, border)
        sizer.Add(self.camera_x_lbl, 0, label_style, border)
        sizer.Add(self.camera_x_entry, 0, wx.RIGHT, border)
        sizer.Add(self.camera_y_lbl, 0, label_style, border)
        sizer.Add(self.camera_y_entry, 0, wx.RIGHT, border)
        sizer.Add(self.camera_zoom_lbl, 0, label_style, border)
        sizer.Add(self.camera_zoom_combobox, 0, wx.RIGHT, border)

        self.SetSizerAndFit(sizer)
