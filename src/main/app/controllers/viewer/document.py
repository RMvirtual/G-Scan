from src.main.documents.processing import DocumentToProcess, DocumentWorkload
from src.main.gui.image_viewer.panels import FileTree


class DocumentController:
    def __init__(self, gui: FileTree):
        self._gui = gui
        self._documents = DocumentWorkload()

    def add_documents(self, file_paths: list[str]) -> None:
        for file_path in file_paths:
            self._documents.pending.append(file_path)

        self._gui.tree.AppendItem(
            parent=self._gui.root_id,
            text=f"Pending ({len(file_paths)})"
        )
