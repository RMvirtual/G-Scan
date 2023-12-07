from __future__ import annotations
from src.main import file_system


class Document:
    def __init__(self) -> None:
        self.short_code = ""
        self.full_name = ""
        self.analysis_code = ""

    def __eq__(self, other: Document) -> bool:
        return self.short_code == other.short_code


class DocumentTypes:
    def __init__(self):
        self.documents = []

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


def load(short_code: str = None, full_name: str = None) -> Document:
    documents = load_all()

    if full_name:
        return documents.from_full_name(full_name)

    elif short_code:
        return documents.from_short_code(short_code)

    else:
        raise ValueError("No Document Type selected.")


def load_all() -> DocumentTypes:
    result = DocumentTypes()
    key_values = _json_contents().items()

    result.documents = [
        _document(short_code, values) for short_code, values in key_values]

    return result


def _document(key: str, values: dict[str, any]) -> Document:
    result = Document()
    result.short_code = key
    result.full_name = values["full_name"]
    result.analysis_code = values["analysis_code"]

    return result


def _json_contents() -> dict[str, any]:
    return file_system.load_json(file_system.document_types_path())