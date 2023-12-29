import dataclasses

from models.departments import Department
from models.document_type import DocumentType


@dataclasses.dataclass
class UserSettings:
    username: str = ""
    scan_dir: str = ""
    dest_dir: str = ""
    department: Department|None = None
    document_type: DocumentType|None = None
