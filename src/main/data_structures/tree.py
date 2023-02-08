from __future__ import annotations
import wx


class AbstractNode:
    def __init__(self, parent: AbstractNode = None, label: str = ""):
        self._parent = None
        self._children = []
        self._label = label

        if parent:
            parent.add(self)

        else:
            self._node_id = None

    def add(self, node: AbstractNode) -> AbstractNode:
        if node.has_parent():
            node.detach()

        node.node_id = self.root.control.AppendItem(
            parent=self.node_id, text=node.label)

        node.parent = self
        self.children.append(node)

        return node

    def detach(self) -> AbstractNode:
        if self.parent:
            self.parent.children.remove(self)

        self.root.control.Delete(item=self.node_id)
        self.parent = None
        self.node_id = None

        return self

    def node_by_id(self, node_id: wx.TreeItemId) -> AbstractNode or None:
        for child in self.children:
            if child.is_node(node_id):
                return child

            if child.has_children():
                return child.node_by_id(node_id)

        return None

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, new_label: str) -> None:
        self._label = new_label

    @property
    def root(self) -> AbstractRoot:
        return self.parent.root

    @property
    def parent(self) -> AbstractNode:
        return self._parent

    @parent.setter
    def parent(self, new_parent: AbstractNode) -> None:
        self._parent = new_parent

    @property
    def children(self) -> list[AbstractNode]:
        return self._children

    @children.setter
    def children(self, new_children: list[AbstractNode]) -> None:
        self._children = new_children

    @property
    def node_id(self) -> wx.TreeItemId:
        return self._node_id

    @node_id.setter
    def node_id(self, new_node_id: wx.TreeItemId) -> None:
        self._node_id = new_node_id

    def is_root(self) -> bool:
        raise NotImplementedError

    def is_branch(self) -> bool:
        raise NotImplementedError

    def is_leaf(self) -> bool:
        raise NotImplementedError

    def has_children(self) -> bool:
        return bool(self._children)

    def has_parent(self) -> bool:
        return self._parent is not None

    def is_node(self, node_id: wx.TreeItemId) -> bool:
        return self._node_id == node_id


class AbstractRoot(AbstractNode):
    """Requires a wx.TreeCtrl object to plug into to create node ID
    references.
    """
    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        super().__init__()
        self._control = tree_control
        self.node_id = self._control.AddRoot(text="Document Root")

    @property
    def root(self) -> AbstractRoot:
        return self

    @property
    def control(self) -> wx.TreeCtrl:
        return self._control

    def is_root(self) -> bool:
        return True

    def is_branch(self) -> bool:
        return False

    def is_leaf(self) -> bool:
        return False


class AbstractBranch(AbstractNode):
    def __init__(self, parent: AbstractNode, label: str = "") -> None:
        super().__init__(parent=parent, label=label)

    def is_root(self) -> bool:
        return False

    def is_branch(self) -> bool:
        return True

    def is_leaf(self) -> bool:
        return False


class AbstractLeaf(AbstractNode):
    def __init__(
            self, parent: AbstractNode, label: str = "",
            data: list[any] = None
    ) -> None:
        super().__init__(parent=parent, label=label)

        self.data = data if data else []

    def is_root(self) -> bool:
        return False

    def is_branch(self) -> bool:
        return False

    def is_leaf(self) -> bool:
        return True

    def can_split(self) -> bool:
        return len(self.data) > 1

    def split_all(self) -> None:
        while self.can_split():
            self.split_range(start=1, stop=2)

    def split_range(self, start: int, stop: int) -> None:
        if not self.is_valid_range(start, stop):
            raise ValueError(f"Invalid range: {start}, {stop}.")

        new_leaf = AbstractLeaf(parent=self.parent, label=self.label)
        new_leaf.data = self.data[start:stop]
        del self.data[start:stop]

    def is_valid_range(self, start: int, stop: int) -> bool:
        start_invalid = start < 0 or start > len(self.data) - 1
        stop_invalid = stop < start or stop > len(self.data)

        return not start_invalid or stop_invalid
