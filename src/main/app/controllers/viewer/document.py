import ntpath
import wx

from src.main import file_system
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main.data_structures.tree import *
from src.main.documents import (
    Document, DocumentBranch, DocumentLeaf, DocumentTree, JobBranch,
    PendingBranch, PendingLeaf, rendering
)

from src.main.gui import Viewer
from src.main.gui.dialogs.document_split import DocumentSplitDialog
from src.main.gui.viewer.document_tree import DocumentTreePanel


class DocumentController:
    def __init__(self, gui: Viewer):
        self._gui = gui
        self._page_view = PageViewController(gui=self._gui.page_view)

        self._document_tree = DocumentTree(
            tree_control=self._gui.file_tree.tree)
        self._page_view.hide_all_widgets()
        self._currently_viewed = None
        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED, handler=self.on_item_selection)

        """
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_ITEM_ACTIVATED, handler=self.on_item_selection)
        """

        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_extract_pages(callback=self.on_split_pages)

    def import_files(self):
        files = file_system.file_import_dialog()

        if files:
            results = self.add_pending_files(paths=files)
            self._set_currently_viewed(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def submit(self, reference: str, document_type: Document) -> None:
        if self._document_tree.contains_branch(reference):
            job_branch = self._document_tree.branch(reference)

            if job_branch.contains_branch(document_type):
                print(f"Contains {document_type.short_code}")

            else:
                print(f"Does not contain {document_type.short_code}")

        else:
            print("Does not contain reference.")
            job_branch = self._document_tree.create_job_branch(
                reference=reference)

            document_branch = job_branch.create_branch(
                document_type=document_type)

            document_branch.add(self._currently_viewed)

        self._gui.file_tree.tree.ExpandAll()

    def on_split_pages(self, event: wx.EVT_BUTTON) -> None:
        with DocumentSplitDialog(len(self._currently_viewed.data)) as dialog:
            option = dialog.ShowModal()

            if option == DocumentSplitDialog.SPLIT_ALL:
                self._currently_viewed.split_all()

            elif option == DocumentSplitDialog.SPLIT_RANGE:
                range = dialog.page_range()
                self._currently_viewed.split_range(
                    start=range[0] - 1, stop=range[1])

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if selections:
            for selection in selections:
                node = self._document_tree.child_by_id(node_id=selection)
                node.detach()

            self._page_view.clear_display()

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        self._display_node_to_view(page_no=event.Position - 1)

    def on_item_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if len(selections) == 1:
            print("One item selected.")
            node = self._document_tree.child_by_id(node_id=selections[0])

            if node.is_leaf():
                self._set_currently_viewed(node)

            elif node.is_branch():
                self._gui.file_tree.tree.Expand(item=node.node_id)
                self._page_view.hide_all_widgets()
                self._clear_node_to_view()

        elif len(selections) > 1:
            self._page_view.hide_split_button()

        else:
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _set_currently_viewed(self, node: AbstractLeaf) -> None:
        if not node.is_leaf():
            raise ValueError("Node is not viewable leaf.")

        self._currently_viewed = node

        self._page_view.show_all_widgets()
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
        result = [self._create_pending_leaf(file_path=path) for path in paths]
        self._gui.file_tree.tree.ExpandAll()

        return result

    def _create_pending_leaf(self, file_path: str) -> PendingLeaf:
        return PendingLeaf(
            parent=self._document_tree.pending_branch,
            file_name=ntpath.basename(file_path),
            data=rendering.render_images(file_path=file_path)
        )
