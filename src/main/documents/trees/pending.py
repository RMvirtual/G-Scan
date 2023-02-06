from __future__ import annotations

import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *
from src.main.documents.trees.root import TreeRoot


class PendingTree:
    def __init__(self, absolute_root: TreeRoot) -> None:
        self.absolute_root = absolute_root
        self.root = PendingRoot(absolute_root=self.absolute_root)
        self.absolute_root.control.Expand(item=self.root.node_id)

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        return [self.add_pending(path) for path in paths]

    def add_pending(self, file_path: str) -> PendingLeaf:
        new_leaf = PendingLeaf(parent_node=self.root, file_path=file_path)

        new_leaf.node_id = self.absolute_root.control.AppendItem(
            parent=new_leaf.parent_node.node_id, text=new_leaf.file_name)

        return new_leaf

    def _refresh_count(self) -> None:
        self.tree_control.SetItemText(
            item=self.pending_root,
            text=f"Pending Items ({len(self.pending)})"
        )


class PendingRoot(AbstractNode):
    def __init__(self, absolute_root: TreeRoot):
        super().__init__(parent=None)
        self.absolute_root = absolute_root

        self.node_id = self.absolute_root.control.AppendItem(
            parent=self.absolute_root.node_id, text="Pending")

    def is_root(self) -> bool:
        return True

    def is_child_node(self) -> bool:
        return False

    def append(self, leaf: PendingLeaf) -> None:
        leaf.node_id = self.absolute_root.control.AppendItem(
            parent=self.node_id, text=leaf.file_name)

        self.child_nodes.append(leaf)


class PendingLeaf(AbstractNode):
    def __init__(self, parent_node: PendingRoot, file_path: str):
        super().__init__(parent=parent_node)

        self.file_path = file_path
        self.set_parent_node(parent_node)
        self.images = render_images(file_path=file_path)

    @property
    def file_name(self) -> str:
        return ntpath.basename(self.file_path)

    def is_root(self) -> bool:
        return False

    def is_child_node(self) -> bool:
        return self.parent_node is not None

    def set_parent_node(self, node: AbstractNode) -> None:
        self.parent_node = node
        self.parent_node.append(self)
