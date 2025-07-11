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

        self.input_bar = DocumentEntryToolbar(self)
        self.page_view = PageCanvas(self)
        self.file_tree = DocumentTreePanel(self)
        self.exit_btn = wx.Button(self, label="Exit")

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
            self.exit_btn,
            proportion=0,
            flag=wx.ALIGN_RIGHT | wx.BOTTOM,
            border=5,
        )

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
