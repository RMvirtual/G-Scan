import wx
from src.main.documents.document_tree import (
    PendingDocument, PendingDocuments, DocumentTree)

from src.main.gui import ImageViewer
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main import file_system


class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(page_canvas=self._gui.page_view)
        self.pending = PendingDocuments(self._gui.file_tree.tree)
        self.document_tree = DocumentTree(self._gui.file_tree.tree)

        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED,
            handler=self.on_file_tree_selection
        )

    def on_file_tree_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if len(selections) == 1:
            print("One Item Selected")

        elif len(selections) > 1:
            print("Multiple items selected.")

        else:
            print("No items selected apparently.")

    def import_files(self):
        files = file_system.request_files_to_import()

        if not files:
            return

        self._process_files(files)

    def import_as(self) -> None:
        print("Michelin Mode")

    def add_pending_files(self, paths: list[str]) -> list[PendingDocument]:
        result = [self.add_pending_file(path) for path in paths]

        return result

    def add_pending_file(self, path: str) -> PendingDocument:
        return self.document_tree.add_pending(file_path=path)

    def _process_files(self, file_paths: list[str]) -> None:
        result = self.add_pending_files(paths=file_paths)
        self._page_view.load_image(result[0].images[0])
