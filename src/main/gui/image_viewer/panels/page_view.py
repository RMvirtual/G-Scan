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
        self._rename_zoom_to_fit_widget()
        self.delete_button = wx.Button(parent=self.ToolBar, label="Delete")

        self.page_no = wx.SpinCtrl(
            parent=self.ToolBar, value="0",
            style=wx.SP_ARROW_KEYS|wx.SP_HORIZONTAL
        )

        self.page_quantity = wx.TextCtrl(
            parent=self.ToolBar, value="Total Pages: 0", style=wx.TE_READONLY)

        self.extract_pages = wx.Button(
            parent=self.ToolBar, label="Extract Pages")

        additional_tools = [
            self.page_no, self.page_quantity, self.delete_button,
            self.extract_pages
        ]

        for tool in additional_tools:
            self.ToolBar.AddControl(control=tool)

        self.ToolBar.Realize()

    def set_total_pages(self, quantity: int or str) -> None:
        self.page_quantity.SetValue(f"Total Pages: {quantity}")
        self.page_no.SetMin(1)
        self.page_no.SetMax(quantity)

    def _rename_zoom_to_fit_widget(self) -> None:
        zoom_to_fit = self.ToolBar.GetToolByPos(5).GetControl()
        zoom_to_fit.Label = "Fit To Page"

    @property
    def canvas(self) -> FloatCanvas:
        return self.Canvas

    @property
    def toolbar(self) -> None:
        return self.ToolBar