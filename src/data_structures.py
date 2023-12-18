from __future__ import annotations


class AbstractNode:
    def __init__(self, parent: AbstractNode = None, label: str = ""):
        self._parent = None
        self._children = []
        self._label = label

        if parent:
            parent.add(self)

    def add(self, node: AbstractNode) -> AbstractNode:
        if node.has_parent():
            node.detach()

        node.parent = self
        self.children.append(node)

        return node

    def detach(self) -> AbstractNode:
        if self._parent:
            self._parent.children.remove(self)

        self._parent = None

        return self

    def child_by_id(self, node_id: int) -> AbstractNode or None:
        for child in self.children:
            if child.node_id == node_id:
                return child

            if child.has_children():
                grandchild = child.child_by_id(node_id)

                if grandchild and grandchild.node_id == node_id:
                    return grandchild

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
    def node_id(self) -> int:
        return id(self)

    def is_root(self) -> bool:
        raise NotImplementedError

    def is_branch(self) -> bool:
        raise NotImplementedError

    def is_leaf(self) -> bool:
        raise NotImplementedError

    def is_empty(self) -> bool:
        return not self._children

    def has_parent(self) -> bool:
        return self._parent is not None

    def has_children(self) -> bool:
        return len(self._children) > 0

    def __eq__(self, other: AbstractNode) -> bool:
        return self.node_id == other.node_id


class AbstractRoot(AbstractNode):
    def __init__(self, label: str = "") -> None:
        super().__init__(parent=None, label=label)

    @property
    def root(self) -> AbstractRoot:
        return self

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

    def split_all(self) -> list[AbstractLeaf]:
        result = []

        while self.can_split():
            result.append(self.split_range(start=1, stop=2))

        return result

    def split_range(self, start: int, stop: int) -> AbstractLeaf:
        if not self.is_valid_range(start, stop):
            raise ValueError(f"Invalid range: {start}, {stop}.")

        result = AbstractLeaf(parent=self.parent, label=self.label)
        result.data = self.data[start:stop]
        del self.data[start:stop]

        return result

    def is_valid_range(self, start: int, stop: int) -> bool:
        start_invalid = start < 0 or start > len(self.data) - 1
        stop_invalid = stop < start or stop > len(self.data)

        return not (start_invalid or stop_invalid)
