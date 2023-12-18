from data_structures import (
    AbstractBranch, AbstractRoot, AbstractLeaf)


class PendingBranch(AbstractBranch):
    def __init__(self, parent: AbstractRoot) -> None:
        super().__init__(parent=parent, label="Pending")


class PendingLeaf(AbstractLeaf):
    def __init__(
            self, parent: PendingBranch, file_name: str = "",
            data: list[any] = None
    ) -> None:
        super().__init__(parent=parent, label=file_name, data=data)
