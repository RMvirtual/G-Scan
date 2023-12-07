from __future__ import annotations
from data_structures.tree_node import AbstractNode


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
