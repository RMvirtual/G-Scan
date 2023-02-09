from __future__ import annotations
from src.main.data_structures.tree_node import AbstractNode


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

        return not (start_invalid or stop_invalid)
