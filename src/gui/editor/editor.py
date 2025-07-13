import wx

from gui.editor.canvas import PageCanvas
from gui.editor.entry_toolbar import DocumentEntryToolbar
from gui.editor.menu_bar import TopMenuBar


class EditorPanel(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.entry_toolbar = DocumentEntryToolbar(self)
        self.page_canvas = PageCanvas(self)

        tree_style = (
            wx.TR_HIDE_ROOT
            | wx.TR_TWIST_BUTTONS
            | wx.TR_HAS_BUTTONS
            | wx.TR_NO_LINES
            | wx.TR_MULTIPLE
        )

        self.tree_ctrl = wx.TreeCtrl(self, style=tree_style)

        self.upload_btn = wx.Button(parent=self, label="Upload to FCL")
        self.exit_btn = wx.Button(self, label="Exit")
        self.menu_bar = TopMenuBar()
        parent.SetMenuBar(self.menu_bar)

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        border = 5
        full_width = wx.EXPAND | wx.LEFT | wx.RIGHT

        sizer.Add(self.entry_toolbar, 0, full_width, border)

        tree_sizer = wx.BoxSizer(orient=wx.VERTICAL)

        tree_sizer.Add(
            window=self.upload_btn,
            proportion=0,
            flag=wx.ALIGN_LEFT | wx.ALL,
            border=5,
        )

        tree_sizer.Add(
            window=self.tree_ctrl,
            proportion=1,
            flag=wx.EXPAND | wx.VERTICAL,
            border=5,
        )

        midsection = wx.BoxSizer(orient=wx.HORIZONTAL)
        midsection.Add(self.page_canvas, 3, wx.EXPAND | wx.ALL, border)
        midsection.Add(tree_sizer, 1, wx.EXPAND | wx.ALL, border)
        sizer.Add(midsection, 1, full_width, border)
        sizer.Add(self.exit_btn, 0, wx.ALIGN_RIGHT | wx.BOTTOM, border)

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
