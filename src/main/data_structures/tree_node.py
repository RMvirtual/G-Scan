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
        # Logic not working in here for some reason.

        children_names = [child.label for child in self.children]
        print(f"All children: {children_names}")

        for child in self.children:
            print(f"Current Child: {child} {child.node_id}")
            if child.node_id == node_id:
                return child

            if not child.is_empty():
                return child.child_by_id(node_id)

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

    def __eq__(self, other: AbstractNode) -> bool:
        return self.node_id == other.node_id
