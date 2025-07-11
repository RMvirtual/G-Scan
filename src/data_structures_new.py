from __future__ import annotations

import abc
from typing import Iterator

import wx

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
        self, name: str, document_type: DocumentType
    ) -> DocumentEntry:
        return self.pending.create_document(name, document_type)

    def remove(self, entry: Branch) -> None:
        if entry is not self.pending or entry not in self.jobs:
            raise ValueError(f"Cannot remove entry {entry.name}")


class Branch(abc.ABC):
    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name
        self.documents = []
        self.gui_id: wx.TreeItemId | None = None

    def create_document_entry(
        self, name: str, document_type: DocumentType
    ) -> DocumentEntry:
        result = DocumentEntry(self, name, document_type)
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
        super().__init__("Pending")

    def create_document(
        self, name: str, document_type: DocumentType
    ) -> DocumentEntry:
        result = DocumentEntry(self, name, document_type)
        self.documents.append(result)

        return result


class JobBranch(Branch):
    def __init__(self, reference: str) -> None:
        super().__init__(reference)


class DocumentTypeBranch(Branch):
    def __init__(self, type_name: str) -> None:
        super().__init__(type_name)


class DocumentEntry:
    def __init__(
        self, parent: Branch, name: str, document_type: DocumentType
    ) -> None:
        self.parent = parent
        self.name = name
        self.type = document_type
        self.pages = []
        self.gui_id: wx.TreeItemId | None = None
