from __future__ import annotations

import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class PendingDocument:
    def __init__(self, file_path: str):
        self.file_name = ntpath.basename(file_path)
        self.tree_item = wx.TreeItemId()
        self.images = render_images(file_path)

    def __len__(self) -> int:
        return len(self.images)


class PendingDocuments:
    def __init__(self, tree: wx.TreeCtrl):
        self.tree = tree
        self.pending: list[PendingDocument] = []

        self.pending_category: wx.TreeItemId = self.tree.AppendItem(
            parent=self.tree.GetRootItem(), text="")

    def add_pending(self, file_path: str) -> PendingDocument:
        result = PendingDocument(file_path=file_path)

        result.tree_item = self.tree.AppendItem(
            parent=self.pending_category,
            text=f"{result.file_name} ({len(result)})"
        )

        self.tree.Expand(self.pending_category)
        self.pending.append(result)

        return result

    def from_file_name(self, file_name: str) -> PendingDocument:
        matching_items = filter(
            lambda x: x.file_name == file_name, self.pending)

        return next(matching_items)

    def __len__(self) -> int:
        return len(self.pending)

    def __getitem__(self, index: int) -> PendingDocument:
        return self.pending[index]


class DocumentTrees:
    """
    Provides support for multiple tree roots with one underlying
    general root.
    """

    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        self.tree_control = tree_control
        self.absolute_root = self.tree_control.AddRoot(text="All Files")

        self.pending_root = DocumentRoot(
            tree_control=tree_control, text="Pending")

        self.tree_control.ExpandAll()

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        return [self.add_pending(path) for path in paths]

    def add_pending(self, file_path: str) -> PendingLeaf:
        new_leaf = PendingLeaf(parent_node=self.pending_root)

        new_leaf.node_id = self.tree_control.AppendItem(
            parent=new_leaf.parent_node.node_id, text=file_path
        )

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


