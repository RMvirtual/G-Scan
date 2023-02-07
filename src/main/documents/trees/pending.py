from src.main.documents.trees.interfaces import (
    AbstractBranch, AbstractDocumentRoot, AbstractLeaf)


class PendingBranch(AbstractBranch):
    def __init__(self, parent: AbstractDocumentRoot) -> None:
        super().__init__(parent=parent, label="Pending")


class PendingLeaf(AbstractLeaf):
    def __init__(self, parent: PendingBranch, file_name: str = "") -> None:
        super().__init__(parent=parent, label=file_name)
