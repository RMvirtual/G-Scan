from src.main.documents.processing import (
    DocumentToProcess, DocumentWorkload, PendingDocument, PendingDocuments)

from src.main.gui.image_viewer.panels import FileTree


class DocumentController:
    def __init__(self, gui: FileTree):
        self._gui = gui
        self._documents = DocumentWorkload()
        self._pending = PendingDocuments(self._gui.tree)

    def add_files(self, file_paths: list[str]) -> None:
        for file_path in file_paths:
            self.add_file(file_path=file_path)

    def add_file(self, file_path: str) -> None:
        self._pending.add_file(file_name=file_path)

    def add_pending(self, document: DocumentToProcess) -> None:
        ...

    @staticmethod
    def _document(file_path: str) -> DocumentToProcess:
        result = DocumentToProcess()
        result.file_path = file_path
        result.tree_item_id = None

        return result
