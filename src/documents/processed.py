from __future__ import annotations

from data_structures import (
    AbstractBranch, AbstractLeaf, AbstractRoot)

from documents.format import AbstractReference
from documents.document_types import Document


class JobBranch(AbstractBranch):
    def __init__(
            self, parent: AbstractRoot, reference: AbstractReference) -> None:
        super().__init__(parent=parent, label=str(reference))
        self.reference = reference
        self.document_branches: list[DocumentBranch] = []

    def set_reference(self, new_reference: AbstractReference) -> None:
        self.reference = new_reference
        self.label = str(new_reference)

    def create_branch(self, document_type: Document) -> DocumentBranch:
        result = DocumentBranch(parent=self, document_type=document_type)
        self.document_branches.append(result)

        return result

    def branch(self, document_type: Document) -> DocumentBranch:
        if not self.contains_branch(document_type):
            raise ValueError(
                f"Document Type {document_type.short_code} not found")

        return self.matching_branches(document_type)[0]

    def contains_branch(self, document_type: Document) -> bool:
        return bool(self.matching_branches(document_type))

    def matching_branches(self, document: Document) -> list[DocumentBranch]:
        return [
            branch for branch in self.document_branches
            if branch.document_type == document
        ]


class DocumentBranch(AbstractBranch):
    def __init__(self, parent: JobBranch, document_type: Document) -> None:
        super().__init__(parent=parent, label=document_type.full_name)
        self.document_type = document_type

    def set_type(self, new_type: Document) -> None:
        self.document_type = new_type
        self.label = new_type.full_name


class DocumentLeaf(AbstractLeaf):
    def __init__(
            self, parent: DocumentBranch, file_name: str = "",
            data: list[any] = None
     ) -> None:
        super().__init__(parent=parent, label=file_name, data=data)
