import wx


class TreeRoot:
    def __init__(self, tree_control: wx.TreeCtrl):
        self.control = tree_control
        self._node_id = self.control.AddRoot(text="All Files")

    @property
    def node_id(self) -> wx.TreeItemId:
        return self._node_id
