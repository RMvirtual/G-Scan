from data_structures import AbstractRoot
from documents.pending import PendingBranch
from documents.processed import JobBranch
from job_references import GrReference

class DocumentTree(AbstractRoot):
    def __init__(self) -> None:
        super().__init__(label="All Files")

        self.pending_branch = PendingBranch(parent=self)
        self.job_branches: list[JobBranch] = []

    def create_job_branch(self, reference: GrReference) -> JobBranch:
        result = JobBranch(parent=self, reference=reference)
        self.job_branches.append(result)

        return result

    def branch(self, reference: GrReference) -> JobBranch:
        return self.matching_branches(reference)[0]

    def contains_branch(self, reference: GrReference) -> bool:
        return bool(self.matching_branches(reference))

    def matching_branches(
            self, reference: GrReference) -> list[JobBranch]:
        return [
            branch for branch in self.job_branches
            if branch.reference == reference
        ]
