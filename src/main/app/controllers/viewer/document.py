import wx

from src.main import file_system
from src.main.app.controllers.viewer.document_tree import (
    DocumentTreeController)

from src.main.app.controllers.viewer.page_view import PageViewController
from src.main.data_structures import AbstractNode, AbstractLeaf
from src.main.documents import Document
from src.main.documents.trees import PendingLeaf
from src.main.gui import Viewer
from src.main.documents.references import JobReference

class DocumentController:
    def __init__(self, gui: Viewer):
        self._gui = gui
        self._page_view = PageViewController(self._gui.page_view)
        self._document_tree = DocumentTreeController(self._gui.file_tree.tree)
        self._bind_callbacks()

        self._page_view.hide_all_widgets()
        self._currently_viewed = None

    def _bind_callbacks(self) -> None:
        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_split_pages(callback=self.on_split_pages)
        self._document_tree.bind_selection(callback=self.on_item_selection)

    def import_files(self):
        files = file_system.file_import_dialog()

        if files:
            results = self.add_pending_files(paths=files)
            self._set_currently_viewed(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def submit(self, reference: str, document_type: Document) -> None:
        job_reference = self._create_job_reference(reference)

        if job_reference:
            self._document_tree.create_job_node(
                reference=job_reference,
                document_type=document_type,
                leaf=self._currently_viewed
            )

    @staticmethod
    def _create_job_reference(reference: str) -> JobReference or None:
        try:
            return JobReference(reference)

        except ValueError:
            message_box = wx.MessageDialog(
                parent=None, message=f"Job reference {reference} is invalid.",
                caption="Invalid Job Reference"
            )

            with message_box:
                message_box.ShowModal()

            return None

    def on_split_pages(self, event: wx.EVT_BUTTON) -> None:
        self._document_tree.split_pages(self._currently_viewed)

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        self._document_tree.delete_selected()
        self._page_view.clear_display()

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        self._display_node_to_view(page_no=event.Position - 1)

    def on_item_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._document_tree.selected_items()

        if len(selections) == 1:
            self._on_single_item_selection(node=selections[0])

        elif len(selections) > 1:
            self._on_multiple_item_selections(nodes=selections)

        else:
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _on_single_item_selection(self, node: AbstractNode) -> None:
        if node.is_leaf():
            self._set_currently_viewed(node)

        elif node.is_branch():
            self._document_tree.expand(node)
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _on_multiple_item_selections(self, nodes: list[AbstractNode]) -> None:
        self._page_view.hide_split_button()

    def _set_currently_viewed(self, node: AbstractNode) -> None:
        if not node.is_leaf():
            raise ValueError("Node is not viewable leaf.")

        self._currently_viewed = node

        self._page_view.show_all_widgets()
        self._page_view.set_total_pages(len(self._currently_viewed.data))

        self._display_node_to_view()

    def _clear_node_to_view(self) -> None:
        self._currently_viewed = None
        self._page_view.clear_display()

    def _display_node_to_view(self, page_no: int = 0) -> None:
        self._page_view.load_image(self._currently_viewed.data[page_no])
        self._page_view.set_page_no(page_no + 1)

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        return self._document_tree.add_pending_files(paths)
