import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas
from wx.lib.floatcanvas import FloatCanvas

class PageView(NavCanvas):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(
            parent=parent, ProjectionFun=None,
            BackgroundColor="DARK SLATE BLUE"
        )

        self._initialise_additional_toolbar_buttons()

    def _initialise_additional_toolbar_buttons(self) -> None:
        self.delete_button = wx.Button(parent=self.ToolBar, label="Delete")
        self.ToolBar.AddControl(control=self.delete_button, label="Test")
        self.ToolBar.Realize()

    @property
    def canvas(self) -> FloatCanvas:
        return self.Canvas

    @property
    def toolbar(self) -> None:
        return self.ToolBar