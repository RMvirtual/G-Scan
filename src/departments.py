import dataclasses

from documents import DocumentType


@dataclasses.dataclass(frozen=True)
class Department:
    short_code: str
    full_name: str
    short_name: str
    document_types: list[DocumentType]
