import dataclasses
from documents import DocumentTypes


@dataclasses.dataclass
class Department:
    short_code: str = ""
    full_name: str = ""
    short_name: str = ""
    document_types: DocumentTypes = DocumentTypes()

