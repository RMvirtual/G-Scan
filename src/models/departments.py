import dataclasses
from models.document_type import DocumentType


@dataclasses.dataclass
class Department:
    short_code: str
    full_name: str
    short_name: str
    document_types: list[DocumentType]
