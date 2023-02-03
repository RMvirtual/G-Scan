from src.main.departments import Department, Departments
from src.main.documents import Document


class ImageViewerConfiguration:
    def __init__(self) -> None:
        self.scan_directory: str = ""
        self.dest_directory: str = ""
        self.department: Department or None = None
        self.document_type: Document or None = None
        self.all_departments: Departments or None = None
