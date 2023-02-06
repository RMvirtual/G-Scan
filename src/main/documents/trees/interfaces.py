from __future__ import annotations

import ntpath
import wx
from src.main.documents.rendering.rendering import render_images


class AbstractNode:
    def __init__(self, parent: AbstractNode or None):
        self.parent_node = parent
        self.child_nodes: list[AbstractNode] = []
        self._node_id = None

    @property
    def node_id(self) -> wx.TreeItemId:
        return self._node_id

    @node_id.setter
    def node_id(self, new_node_id) -> None:
        self._node_id = new_node_id

    def is_root(self) -> bool:
        raise NotImplementedError()

    def is_child_node(self) -> bool:
        raise NotImplementedError()

    def is_parent_node(self) -> bool:
        return bool(self.child_nodes)

    def is_leaf_node(self) -> bool:
        return not self.child_nodes


class PendingRoot(AbstractNode):
    def __init__(self, tree_control: wx.TreeCtrl, text: str):
        super().__init__(parent=None)
        self.tree_control = tree_control

        self.node_id = self.tree_control.AppendItem(
            parent=tree_control.GetRootItem(), text=text)

    def is_root(self) -> bool:
        return True

    def is_child_node(self) -> bool:
        return False

    def append_child(self, leaf: PendingLeaf) -> None:
        self.child_nodes.append(leaf)



class DocumentRoot(AbstractNode):
    def __init__(self, tree_control: wx.TreeCtrl, text: str):
        super().__init__(parent=None)
        self.tree_control = tree_control

        self.node_id = self.tree_control.AppendItem(
            parent=tree_control.GetRootItem(), text=text)

    def is_root(self) -> bool:
        return True

    def is_child_node(self) -> bool:
        return False

    def append_child(self) -> AbstractNode:
        ...


class DocumentNode(AbstractNode):
    def __init__(self, parent_node: AbstractNode):
        super().__init__(parent=parent_node)
        self.parent_node = parent_node

    def is_root(self) -> bool:
        return False

    def is_child_node(self) -> bool:
        return self.parent_node is not None


class JobReferenceNode(DocumentRoot):
    def __init__(self, tree_control: wx.TreeCtrl, reference: str):
        super().__init__(tree_control, reference)
        self.reference = reference


class PaperworkNode(DocumentNode):
    def __init__(self, parent_node: JobReferenceNode):
        super().__init__(parent_node)


class DocumentLeaf(DocumentNode):
    def __init__(self, parent_node) -> None:
        super().__init__(parent_node)


class PendingLeaf(DocumentNode):
    def __init__(self, parent_node: PendingRoot, file_path: str):
        super().__init__(parent_node=parent_node)

        self.file_name = file_path
        self.images = render_images(file_path=file_path)
