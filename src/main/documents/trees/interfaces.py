from __future__ import annotations
import wx


class AbstractNode:
    def __init__(self, parent: AbstractNode or None):
        self._parent_node = parent
        self.child_nodes: list[AbstractNode] = []
        self._node_id = None

    @property
    def parent_node(self) -> AbstractNode:
        return self._parent_node

    @parent_node.setter
    def parent_node(self, new_parent: AbstractNode) -> None:
        self._parent_node = new_parent

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
