import wx
from src.main.gui import fonts


class FileTree(wx.Panel):
    def __init__(self, parent: wx.Window):
        super(FileTree, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()


    def _initialise_widgets(self) -> None:
        self._title = wx.StaticText(parent=self, label="Jobs")
        self._title.SetFont(fonts.font(point_size=30, bold=True))

        self.upload_to_fcl = wx.Button(parent=self, label="Upload to FCL")
        self._initialise_tree()

    def _initialise_tree(self) -> None:
        tree_style = (
            wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS|wx.TR_HAS_BUTTONS
            |wx.TR_NO_LINES|wx.TR_MULTIPLE
        )

        self.tree = wx.TreeCtrl(parent=self, style=tree_style)
        self.tree.ExpandAll()

        self.root_id = self.tree.AddRoot(text="All Files")

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self._title, proportion=0,
            flag=wx.ALIGN_CENTRE_HORIZONTAL|wx.ALL, border=5
        )

        sizer.Add(
            window=self.upload_to_fcl, proportion=0,
            flag=wx.ALIGN_LEFT|wx.ALL, border=5
        )

        sizer.Add(
            window=self.tree, proportion=1,
            flag=wx.EXPAND|wx.VERTICAL, border=5
        )

        self.SetSizer(sizer)

    def add_to_pending(self) -> None:
        ...