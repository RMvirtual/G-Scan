from src.main.gui.widgets.frame import Frame
import wx


class ImageViewer(Frame):
    def __init__(self, size):
        super().__init__(size=size, title="Paperwork Viewer")
        self._initialise_widgets()
        self.Show()

    def _initialise_widgets(self) -> None:
        self.SetBackgroundColour("WHITE")

        self._input_panel = wx.Panel(parent=self)

        self._reference_input_label = wx.StaticText(
            parent=self._input_panel, label="Please enter job reference:")

        self._job_reference_input = wx.TextCtrl(parent=self._input_panel)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._reference_input_label)
        sizer.Add(self._job_reference_input)

        sizer.SetSizeHints(self._input_panel)
        self._input_panel.SetSizer(sizer)
        self.SetSizer(sizer)
