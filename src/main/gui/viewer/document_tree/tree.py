import wx


class DocumentTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent: wx.Window) -> None:
        style = (
            wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS|wx.TR_HAS_BUTTONS|
            wx.TR_NO_LINES|wx.TR_MULTIPLE
        )

        super().__init__(parent=parent, style=style)

    def get_node_id(self, tree_handle: wx.TreeItemId) -> int:
        return self.GetItemData(item=tree_handle)

    def get_item_handle(self, node_id: int) -> wx.TreeItemId:
        root_handle = self.GetRootItem()

        if self.GetItemData(item=root_handle) == node_id:
            return root_handle

        child = self._find_child_handle(node_id=node_id, root_id=root_handle)

        if not child.IsOk():
            raise ValueError(f"Node ID {node_id} does not exist in tree.")

        return child

    def _find_child_handle(
            self, node_id: int, root_id: wx.TreeItemId) -> wx.TreeItemId:
        item, cookie = self.GetFirstChild(item=root_id)

        while item.IsOk():
            data = self.GetItemData(item)

            if data == node_id:
                return item

            if self.ItemHasChildren(item):
                match = self._find_child_handle(node_id=node_id, root_id=item)

                if match.IsOk():
                    return match

            item, cookie = self.GetNextChild(root_id, cookie)

        return wx.TreeItemId()