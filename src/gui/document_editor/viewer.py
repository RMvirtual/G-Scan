import wx

from gui.document_editor.canvas import PageCanvas
from gui.document_editor.document_tree import DocumentTreePanel
from gui.document_editor.entry_toolbar import DocumentEntryToolbar
from gui.document_editor.file_menu import FileMenu


class Viewer(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.file_menu = FileMenu()
        parent.SetMenuBar(self.file_menu)

        self.entry_toolbar = DocumentEntryToolbar(self)
        self.page_canvas = PageCanvas(self)
        self.document_tree_panel = DocumentTreePanel(self)
        self.exit_btn = wx.Button(self, label="Exit")

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        border = 5
        full_width = wx.EXPAND | wx.LEFT | wx.RIGHT

        sizer.Add(self.entry_toolbar, 0, full_width, border)
        midsection = wx.BoxSizer(orient=wx.HORIZONTAL)
        midsection.Add(self.page_canvas, 3, wx.EXPAND | wx.ALL, border)
        midsection.Add(self.document_tree_panel, 1, wx.EXPAND | wx.ALL, border)
        sizer.Add(midsection, 1, full_width, border)
        sizer.Add(self.exit_btn, 0, wx.ALIGN_RIGHT | wx.BOTTOM, border)

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
