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
            parent=self.ToolBar, value="2",
            style=wx.SP_ARROW_KEYS|wx.SP_HORIZONTAL
        )


        self.ToolBar.AddControl(control=self.page_no)
        self.ToolBar.AddControl(control=self.delete_button)
        self.ToolBar.Realize()

    @property
    def canvas(self) -> FloatCanvas:
        return self.Canvas

    @property
    def toolbar(self) -> None:
        return self.ToolBar