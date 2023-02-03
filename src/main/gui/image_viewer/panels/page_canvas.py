import wx
from wx.lib.floatcanvas.NavCanvas import NavCanvas
from wx.lib.floatcanvas import FloatCanvas


class PageCanvas(NavCanvas):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(
            parent=parent, ProjectionFun=None,
            BackgroundColor="DARK SLATE BLUE"
        )

    @property
    def canvas(self) -> FloatCanvas:
        return self.Canvas

