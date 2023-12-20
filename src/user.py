import dataclasses

from departments import Department
from documents import Document


@dataclasses.dataclass
class UserSettings:
    username: str = ""
    scan_dir: str = ""
    dest_dir: str = ""
    department: Department|None = None
    document_type: Document|None = None
