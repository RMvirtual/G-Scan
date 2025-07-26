import wx

from gui.menu_bar import TopMenuBar
from gui.toolbar import Toolbar


class EditorFrame(wx.Frame):
    def __init__(
        self, size: tuple[int, int], position: tuple[int, int]
    ) -> None:
        super().__init__(None, title="", size=size, pos=position)

        self.entry_toolbar = Toolbar(self)
        self.page_canvas = wx.Panel(self)

        self.tree_ctrl = wx.TreeCtrl(
            self,
            style=(
                wx.TR_HIDE_ROOT
                | wx.TR_TWIST_BUTTONS
                | wx.TR_HAS_BUTTONS
                | wx.TR_NO_LINES
                | wx.TR_MULTIPLE
            ),
        )

        self.upload_btn = wx.Button(parent=self, label="Upload to FCL")
        self.exit_btn = wx.Button(self, label="Exit")
        self.menu_bar = TopMenuBar()
        self.SetMenuBar(self.menu_bar)

        # Sizer layout.
        border = 5

        tree_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        tree_sizer.Add(self.upload_btn, 0, wx.ALIGN_LEFT | wx.ALL, border)
        tree_sizer.Add(self.tree_ctrl, 1, wx.EXPAND | wx.VERTICAL, border)

        midsection_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        midsection_sizer.Add(self.page_canvas, 3, wx.EXPAND)
        midsection_sizer.Add(tree_sizer, 1, wx.EXPAND | wx.ALL, border)

        main_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        main_sizer.Add(self.entry_toolbar, 0, wx.EXPAND, border)
        main_sizer.Add(midsection_sizer, 1, wx.EXPAND, border)
        main_sizer.Add(self.exit_btn, 0, wx.ALIGN_RIGHT | wx.BOTTOM, border)

        self.SetSizer(main_sizer)
        self.SetBackgroundColour(colour=wx.LIGHT_GREY)
