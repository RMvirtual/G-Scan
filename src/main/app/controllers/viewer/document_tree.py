import ntpath
import wx
from src.main.data_structures.tree import *

from src.main.gui.viewer.document_tree import (
    DocumentTreePanel, DocumentTreeCtrl)

from src.main.documents import (
    Document, DocumentBranch, DocumentLeaf, DocumentTree, JobBranch,
    PendingBranch, PendingLeaf, rendering
)


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeCtrl):
        self._gui = gui
        self._document_tree = DocumentTree()

        root = self._document_tree.root
        root_id = self._gui.AddRoot(text=root.label, data=root.node_id)

        pending = self._document_tree.pending_branch

        self._gui.AppendItem(
            parent=root_id, text=pending.label, data=pending.node_id)

    def bind_selection(self, callback) -> None:
        self._gui.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)
        # self._gui.Bind(event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = [self._create_pending_leaf(file_path=path) for path in paths]

        # Need to pass results to the document tree ctrl here.

        self._gui.ExpandAll()

        return result

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

        self._gui.ExpandAll()

    def _create_pending_leaf(self, file_path: str) -> PendingLeaf:
        return PendingLeaf(
            parent=self._document_tree.pending_branch,
            file_name=ntpath.basename(file_path),
            data=rendering.render_images(file_path=file_path)
        )

    def get_selected_items(self) -> list[AbstractNode]:
        selections = self._gui.GetSelections()

        result = []

        for selection in selections:
            node_id = self._gui.get_node_id(tree_handle=selection)
            node = self._document_tree.child_by_id(node_id=node_id)

            result.append(node)

        return result

    def split_pages(self, node: AbstractLeaf) -> None:
        with DocumentSplitDialog(len(node.data)) as dialog:
            option = dialog.ShowModal()

            if option == DocumentSplitDialog.SPLIT_ALL:
                node.split_all()

            elif option == DocumentSplitDialog.SPLIT_RANGE:
                range = dialog.page_range()
                node.split_range(start=range[0] - 1, stop=range[1])

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if selections:
            for selection in selections:
                node = self._document_tree.child_by_id(node_id=selection)
                node.detach()

            self._page_view.clear_display()

    def expand(self, node: AbstractNode) -> None:
        tree_handle = self._gui.get_item_handle(node_id=node.node_id)
        self._gui.Expand(item=tree_handle)
