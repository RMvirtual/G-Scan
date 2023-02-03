import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas
from wx.lib.floatcanvas import FloatCanvas

class PageView(NavCanvas):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(
            parent=parent, ProjectionFun=None,
            BackgroundColor="DARK SLATE BLUE"
        )

        self._initialise_toolbar_extensions()

    def _initialise_toolbar_extensions(self) -> None:
        self.delete_button = wx.Button(parent=self.ToolBar, label="Delete")
        self.page_no = wx.SpinCtrl(
            parent=self.ToolBar, value="0",
            style=wx.SP_ARROW_KEYS|wx.SP_HORIZONTAL
        )

        self.page_quantity = wx.TextCtrl(
            parent=self.ToolBar, value="Total Pages: 0",
            style=wx.TE_READONLY
        )

        for tool in [self.delete_button, self.page_no, self.page_quantity]:
            self.ToolBar.AddControl(control=tool)

        self.ToolBar.Realize()

    @property
    def canvas(self) -> FloatCanvas:
        return self.Canvas

    @property
    def toolbar(self) -> None:
        return self.ToolBar