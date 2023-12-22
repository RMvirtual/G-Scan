from __future__ import annotations

from data_structures import AbstractBranch, AbstractLeaf, AbstractRoot
from document_type import DocumentType
from job_references import JobReference


class PendingBranch(AbstractBranch):
    def __init__(self, parent: AbstractRoot) -> None:
        super().__init__(parent=parent, label="Pending")


class PendingLeaf(AbstractLeaf):
    def __init__(
            self, parent: PendingBranch, file_name: str = "",
            data: list[any] = None
    ) -> None:
        super().__init__(parent=parent, label=file_name, data=data)


class JobBranch(AbstractBranch):
    def __init__(
            self, parent: AbstractRoot, reference: JobReference) -> None:
        super().__init__(parent=parent, label=str(reference))
        self.reference = reference
        self.document_branches: list[DocumentBranch] = []

    def set_reference(self, new_reference: JobReference) -> None:
        self.reference = new_reference
        self.label = str(new_reference)

    def create_branch(self, document_type: DocumentType) -> DocumentBranch:
        result = DocumentBranch(parent=self, document_type=document_type)
        self.document_branches.append(result)

        return result

    def branch(self, document_type: DocumentType) -> DocumentBranch:
        if not self.contains_branch(document_type):
            raise ValueError(
                f"Document Type {document_type.short_code} not found")

        return self.matching_branches(document_type)[0]

    def contains_branch(self, document_type: DocumentType) -> bool:
        return bool(self.matching_branches(document_type))

    def matching_branches(self, document: DocumentType) -> list[DocumentBranch]:
        return [
            branch for branch in self.document_branches
            if branch.document_type == document
        ]


class DocumentBranch(AbstractBranch):
    def __init__(self, parent: JobBranch, document_type: DocumentType) -> None:
        super().__init__(parent=parent, label=document_type.full_name)
        self.document_type = document_type

    def set_type(self, new_type: DocumentType) -> None:
        self.document_type = new_type
        self.label = new_type.full_name


class DocumentLeaf(AbstractLeaf):
    def __init__(
            self, parent: DocumentBranch, file_name: str = "",
            data: list[any] = None
     ) -> None:
        super().__init__(parent=parent, label=file_name, data=data)


class DocumentTree(AbstractRoot):
    def __init__(self) -> None:
        super().__init__(label="All Files")

        self.pending_branch = PendingBranch(parent=self)
        self.job_branches: list[JobBranch] = []

    def create_job_branch(self, reference: JobReference) -> JobBranch:
        result = JobBranch(parent=self, reference=reference)
        self.job_branches.append(result)

        return result

    def branch(self, reference: JobReference) -> JobBranch:
        return self.matching_branches(reference)[0]

    def contains_branch(self, reference: JobReference) -> bool:
        return bool(self.matching_branches(reference))

    def matching_branches(self, reference: JobReference) -> list[JobBranch]:
        return [
            branch for branch in self.job_branches
            if branch.reference == reference
        ]
