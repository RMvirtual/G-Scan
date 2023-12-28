import wx

from gui.viewer.document_tree import DocumentTreePanel
from gui.viewer.panels import PageView
from gui.viewer.toolbars import BottomToolbar, FileMenu, UserToolbar


class Viewer(wx.Panel):
    def __init__(self, parent_window: wx.Frame):
        super().__init__(parent=parent_window)

        self.file_menu = FileMenu()
        self.Parent.SetMenuBar(self.file_menu)

        self.input_bar = UserToolbar(self)
        self.page_view = PageView(self)
        self.file_tree = DocumentTreePanel(self)
        self.bottom_bar = BottomToolbar(self)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND|wx.LEFT|wx.RIGHT

        sizer.Add(window=self.input_bar, proportion=0, flag=flags, border=5)

        page_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        page_flags = wx.EXPAND|wx.ALL

        page_sizer.Add(self.page_view, proportion=3, flag=page_flags, border=5)
        page_sizer.Add(self.file_tree, proportion=1, flag=page_flags, border=5)

        sizer.Add(page_sizer, proportion=1, flag=flags, border=5)

        sizer.Add(
            self.bottom_bar, proportion=0, flag=flags|wx.BOTTOM, border=5)

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
