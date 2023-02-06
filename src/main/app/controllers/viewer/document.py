from src.main.documents.processing import PendingDocument, PendingDocuments
from src.main.gui.image_viewer.panels import FileTree


class DocumentController:
    def __init__(self, gui: FileTree):
        self._gui = gui
        self.pending = PendingDocuments(self._gui.tree)

    def on_tree_item(self, event = None) -> None:
        ...

    def add_pending_files(self, file_paths: list[str]) -> None:
        for file_path in file_paths:
            self.add_pending_file(file_path=file_path)

    def add_pending_file(self, file_path: str) -> None:
        self.pending.add_pending(file_path=file_path)