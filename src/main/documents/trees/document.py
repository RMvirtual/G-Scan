import wx
from src.main.documents.trees.interfaces import AbstractRoot, AbstractLeaf
from src.main.documents.trees.pending import PendingBranch
from src.main.documents.trees.processed import *
from src.main.documents.types import Document


class DocumentTree(AbstractRoot):
    """Requires a wx.TreeCtrl object to plug into to create the node
    references.
    """
    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        super().__init__(tree_control=tree_control)

        self.pending_branch = PendingBranch(parent=self)
        self.job_branches: list[JobBranch] = []

    def create_job_branch(self, reference: str) -> None:
        self.job_branches.append(JobBranch(parent=self, reference=reference))

    def branch(self, reference: str) -> JobBranch:
        return self.matching_branches(reference)[0]

    def contains_branch(self, reference: str) -> bool:
        return bool(self.matching_branches(reference))

    def matching_branches(self, reference: str) -> list[JobBranch]:
        return [
            branch for branch in self.job_branches
            if branch.reference == reference
        ]


