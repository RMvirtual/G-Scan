from src.main.documents.trees.interfaces import (
    AbstractBranch, AbstractLeaf, AbstractDocumentRoot)


class JobBranch(AbstractBranch):
    def __init__(self, parent: AbstractDocumentRoot, job_ref: str) -> None:
        super().__init__(parent=parent, label=job_ref)


class PaperworkBranch(AbstractBranch):
    def __init__(self, parent: JobBranch, job_reference: str) -> None:
        super().__init__(parent=parent, label=job_reference)


class PaperworkLeaf(AbstractLeaf):
    def __init__(self, parent: PaperworkBranch, label: str = "") -> None:
        super().__init__(parent=parent, label=label)
