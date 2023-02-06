from src.main.documents.processing import (
    DocumentToProcess, DocumentWorkload, PendingDocument, PendingDocuments)

from src.main.gui.image_viewer.panels import FileTree


class DocumentController:
    def __init__(self, gui: FileTree):
        self._gui = gui
        self.pending = PendingDocuments(self._gui.tree)

    def add_pending_files(self, file_paths: list[str]) -> None:
        for file_path in file_paths:
            self.add_pending_file(file_path=file_path)

    def add_pending_file(self, file_path: str) -> None:
        self.pending.add_file(file_path=file_path)

    @staticmethod
    def _document(file_path: str) -> DocumentToProcess:
        result = DocumentToProcess()
        result.file_path = file_path
        result.tree_item_id = None

        return result
