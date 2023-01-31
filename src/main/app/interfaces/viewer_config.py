from src.main.departments import Department
from src.main.documents import Document


class ImageViewerConfiguration:
    def __init__(self) -> None:
        self.scan_directory: str = ""
        self.dest_directory: str = ""
        self.initial_department: Department or None = None
        self.initial_document_type: Document or None = None
