import wx
from src.main.documents.trees.document_tree import (
    PendingDocument, PendingDocuments, DocumentTrees)

from src.main.gui import ImageViewer
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main import file_system


class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(page_canvas=self._gui.page_view)
        self.document_tree = DocumentTrees(self._gui.file_tree.tree)

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

        if files:
            results = self.document_tree.add_pending_files(paths=files)

            # self._page_view.load_image(results[0].images[0])
            self.document_tree.tree_control.ExpandAll()

    def import_as(self) -> None:
        print("Michelin Mode")
