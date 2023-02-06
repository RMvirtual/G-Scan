from src.main.documents.processing import PendingDocument, PendingDocuments
from src.main.gui.image_viewer.panels import FileTree


class DocumentController:
    def __init__(self, gui: FileTree):
        self._gui = gui
        self.pending = PendingDocuments(self._gui.tree)

    def on_tree_item(self, event = None) -> None:
        ...

    def add_pending_files(self, paths: list[str]) -> list[PendingDocument]:
        return [self.add_pending_file(path) for path in paths]

    def add_pending_file(self, path: str) -> PendingDocument:
        return self.pending.add_pending(file_path=path)