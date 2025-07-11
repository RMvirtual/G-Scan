import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas


class PageCanvas(NavCanvas):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(
            parent=parent,
            ProjectionFun=None,
            BackgroundColor="DARK SLATE BLUE",
        )

        fit_zoom_tool = self.ToolBar.GetToolByPos(5).GetControl()
        fit_zoom_tool.Label = "Fit To Page"

        self.delete_btn = wx.Button(parent=self.ToolBar, label="Delete")

        self.page_no_spin_ctrl = wx.SpinCtrl(
            parent=self.ToolBar,
            value="0",
            style=wx.SP_ARROW_KEYS | wx.SP_HORIZONTAL,
        )

        self.page_qty_text = wx.TextCtrl(
            parent=self.ToolBar, value="Pages: 0", style=wx.TE_READONLY
        )

        self.split_btn = wx.Button(parent=self.ToolBar, label="Split Pages")

        additional_tools = [
            self.page_no_spin_ctrl,
            self.page_qty_text,
            self.delete_btn,
            self.split_btn,
        ]

        for tool in additional_tools:
            self.ToolBar.AddControl(tool)

        self.ToolBar.Realize()
