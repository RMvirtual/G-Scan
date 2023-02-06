from __future__ import annotations

import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *
from src.main.documents.trees.root import TreeRoot


class PendingTree:
    def __init__(self, absolute_root: TreeRoot) -> None:
        self.absolute_root = absolute_root
        self._initialise_root()

    def _initialise_root(self) -> None:
        self.root = PendingRoot(tree=self)
        self.expand_all()

    def node(self, node_id: wx.TreeItemId) -> AbstractNode:
        if node_id == self.root.node_id:
            return self.root

        child_nodes = self.root.child_nodes

        for node in child_nodes:
            if node_id == node.node_id:
                return node

        raise ValueError("Node not found.")

    def add_files(self, paths: list[str]) -> list[PendingLeaf]:
        return [self.add_file(path) for path in paths]

    def add_file(self, file_path: str) -> PendingLeaf:
        result = PendingLeaf(parent_node=self.root, file_path=file_path)
        self._refresh_count()

        return result


    def expand_all(self) -> None:
        self.absolute_root.control.Expand(item=self.root.node_id)

    def _refresh_count(self) -> None:
        self.absolute_root.control.SetItemText(
            item=self.root.node_id,
            text=f"Pending Items ({len(self.root.child_nodes)})"
        )




class PendingRoot(AbstractNode):
    def __init__(self, tree: PendingTree):
        super().__init__(parent=None)

        self.tree = tree
        self.node_id = self.tree.absolute_root.append_subtree(text="Pending")

    def is_root(self) -> bool:
        return True

    def is_child_node(self) -> bool:
        return False

    def append(self, leaf: PendingLeaf) -> None:
        leaf.node_id = self.tree.absolute_root.control.AppendItem(
            parent=self.node_id, text=leaf.file_name)

        self.child_nodes.append(leaf)
        self.tree.expand_all()



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
