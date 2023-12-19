from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Document:
    short_code: str = ""
    full_name: str = ""
    analysis_code: str = ""


class DocumentTypes:
    def __init__(self, documents: list[Document] = None):
        if not documents:
            documents = []

        self.documents = documents

    def __contains__(self, short_code: str) -> bool:
        return len(
            document.short_code == short_code for document in self.documents)

    def __iter__(self):
        return self.documents.__iter__()

    def short_codes(self) -> list[str]:
        return [document.short_code for document in self.documents]

    def full_names(self) -> list[str]:
        return [document.full_name for document in self.documents]

    def from_short_code(self, short_code: str) -> Document:
        for document in self.documents:
            if document.short_code == short_code:
                return document

        self._raise_document_invalid(short_code)

    def from_full_name(self, full_name: str) -> Document:
        for document in self.documents:
            if document.full_name == full_name:
                return document

        self._raise_document_invalid(full_name)

    def _raise_document_invalid(self, document_name: str) -> None:
        raise ValueError(f"Document {document_name} does not exist.")
