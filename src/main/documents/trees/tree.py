import wx
from src.main.data_structures import AbstractRoot
from src.main.documents.trees.pending import PendingBranch
from src.main.documents.trees.processed import JobBranch
from src.main.documents.references import AbstractReference


class DocumentTree(AbstractRoot):
    def __init__(self) -> None:
        super().__init__(label="All Files")

        self.pending_branch = PendingBranch(parent=self)
        self.job_branches: list[JobBranch] = []

    def create_job_branch(self, reference: AbstractReference) -> JobBranch:
        result = JobBranch(parent=self, reference=reference)
        self.job_branches.append(result)

        return result

    def branch(self, reference: AbstractReference) -> JobBranch:
        return self.matching_branches(reference)[0]

    def contains_branch(self, reference: AbstractReference) -> bool:
        return bool(self.matching_branches(reference))

    def matching_branches(
            self, reference: AbstractReference) -> list[JobBranch]:
        return [
            branch for branch in self.job_branches
            if branch.reference == reference
        ]
