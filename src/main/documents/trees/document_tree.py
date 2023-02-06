import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class DocumentTrees:
    """
    Provides support for multiple tree roots with one underlying
    general root.
    """

    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        self.tree_control = tree_control
        self.absolute_root = self.tree_control.AddRoot(text="All Files")

        self.pending_root = PendingRoot(
            tree_control=tree_control, text="Pending")

        self.tree_control.ExpandAll()

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        return [self.add_pending(path) for path in paths]

    def add_pending(self, file_path: str) -> PendingLeaf:
        new_leaf = PendingLeaf(
            parent_node=self.pending_root, file_path=file_path)

        new_leaf.node_id = self.tree_control.AppendItem(
            parent=new_leaf.parent_node.node_id, text=file_path)

        return new_leaf

        file_name = ntpath.basename(file_path)
        tree_item = wx.TreeItemId()
        images = render_images(file_path)

        result = PendingDocument(file_path=file_path)

        result.tree_item = self.tree_control.AppendItem(
            parent=self.pending_root.node_id,
            text=f"{result.file_name} ({len(result)})"
        )

        self.tree_control.Expand(self.pending_root)
        # self.pending.append(result)

        return result

    def _refresh_count(self) -> None:
        self.tree_control.SetItemText(
            item=self.pending_root,
            text=f"Pending Items ({len(self.pending)})"
        )
