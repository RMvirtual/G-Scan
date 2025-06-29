from __future__ import annotations

import abc
from typing import Iterator

from documents import DocumentType


class DocumentTree:
    def __init__(self) -> None:
        self.pending = PendingBranch()
        self.jobs: list[JobBranch] = []

    def create_job_branch(self, reference: str) -> JobBranch:
        result = JobBranch(reference)
        self.jobs.append(result)

        return result

    def create_pending_document(
        self, document_type: DocumentType
    ) -> DocumentEntry:
        return self.pending.create_document(document_type)


class Branch(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

        self.documents = []

    def create_document_entry(
        self, document_type: DocumentType
    ) -> DocumentEntry:
        result = DocumentEntry(self, document_type)
        self.append(result)

        return result

    def append(self, document: DocumentEntry) -> None:
        if document.parent is not None:
            document.parent.remove(document)

        document.parent = self
        self.documents.append(document)

    def remove(self, document: DocumentEntry) -> None:
        if document in self:
            self.documents.remove(document)

        if document.parent is self:
            document.parent = None

    def __iter__(self) -> Iterator[DocumentEntry]:
        return self.documents.__iter__()

    def __len__(self) -> int:
        return len(self.documents)


class PendingBranch(Branch):
    def __init__(self) -> None:
        super().__init__()

    def create_document(self, document_type: DocumentType) -> DocumentEntry:
        result = DocumentEntry(self, document_type)
        self.documents.append(result)

        return result


class JobBranch(Branch):
    def __init__(self, reference: str) -> None:
        super().__init__()

        self.reference = reference


class DocumentEntry:
    def __init__(self, parent: Branch, document_type: DocumentType) -> None:
        self.parent = parent
        self.type = document_type
        self.pages = []
