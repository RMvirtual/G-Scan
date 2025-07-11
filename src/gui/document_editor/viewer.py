import wx

from gui.document_editor.document_tree import DocumentTreePanel
from gui.document_editor.file_menu import FileMenu
from gui.document_editor.panels import PageView
from gui.document_editor.toolbars import BottomToolbar, UserToolbar


class Viewer(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.file_menu = FileMenu()
        parent.SetMenuBar(self.file_menu)

        self.input_bar = UserToolbar(self)
        self.page_view = PageView(self)
        self.file_tree = DocumentTreePanel(self)
        self.bottom_bar = BottomToolbar(self)

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        flags = wx.EXPAND | wx.LEFT | wx.RIGHT

        sizer.Add(window=self.input_bar, proportion=0, flag=flags, border=5)

        page_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        page_flags = wx.EXPAND | wx.ALL

        page_sizer.Add(self.page_view, proportion=3, flag=page_flags, border=5)
        page_sizer.Add(self.file_tree, proportion=1, flag=page_flags, border=5)

        sizer.Add(page_sizer, proportion=1, flag=flags, border=5)

        sizer.Add(
            self.bottom_bar, proportion=0, flag=flags | wx.BOTTOM, border=5
        )

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
