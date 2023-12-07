import wx
from wx.lib.floatcanvas import FloatCanvas
from gui.viewer.panels.page_view import PageView
from gui.viewer.toolbars.user_input import UserToolbar
from gui.viewer.toolbars.bottom_toolbar import BottomToolbar
from gui.viewer.document_tree.panel import DocumentTreePanel
from gui.viewer.toolbars.file_menu import FileMenu


class Viewer(wx.Panel):
    def __init__(self, parent_window: wx.Frame):
        super().__init__(parent=parent_window)
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._initialise_panels()
        self._initialise_sizer()
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)

    def _initialise_panels(self) -> None:
        self.file_menu = FileMenu()
        self.Parent.SetMenuBar(self.file_menu)

        self.input_bar = UserToolbar(self)
        self.page_view = PageView(self)
        self.file_tree = DocumentTreePanel(self)
        self.bottom_bar = BottomToolbar(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND|wx.LEFT|wx.RIGHT

        sizer.Add(window=self.input_bar, proportion=0, flag=flags, border=5)
        sizer.Add(sizer=self._page_sizer(), proportion=1, flag=flags, border=5)

        sizer.Add(
            window=self.bottom_bar,
            proportion=0, flag=flags|wx.BOTTOM, border=5
        )

        self.SetSizer(sizer)

    def _page_sizer(self) -> wx.Sizer:
        result = wx.BoxSizer(orient=wx.HORIZONTAL)
        flags = wx.EXPAND|wx.ALL

        result.Add(window=self.page_view, proportion=3, flag=flags, border=5)
        result.Add(window=self.file_tree, proportion=1, flag=flags, border=5)

        return result