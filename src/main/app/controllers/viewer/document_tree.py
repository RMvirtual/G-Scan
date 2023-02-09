import ntpath
import wx
from src.main.data_structures import AbstractNode, AbstractLeaf

from src.main.documents import (
    Document, DocumentBranch, DocumentLeaf, DocumentTree, JobBranch,
    PendingBranch, PendingLeaf, rendering
)

from src.main.gui.dialogs.page_range import PageRangeDialog
from src.main.gui.viewer.document_tree import DocumentTreeCtrl
from src.main.documents.references import JobReference


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeCtrl):
        self._gui = gui
        self._document_tree = DocumentTree()
        self._initialise_root_node()
        self._append_to_gui(self._document_tree.root.pending_branch)

    def _initialise_root_node(self) -> None:
        root = self._document_tree.root
        self._gui.AddRoot(text=root.label, data=root.node_id)

    def bind_selection(self, callback) -> None:
        self._gui.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)
        # self._gui.Bind(event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)

    def selected_items(self) -> list[AbstractNode]:
        return [
            self._node_from_handle(handle=selection)
            for selection in self._gui.GetSelections() if selection is not None
        ]

    def split_pages(self, node: AbstractLeaf) -> None:
        with PageRangeDialog(max_pages=len(node.data)) as dialog:
            self._on_split_dialog(dialog, node)

    def delete_selected(self) -> None:
        for node in self.selected_items():
            node.detach()
            self._remove_from_gui(node)

    def expand(self, node: AbstractNode) -> None:
        self._gui.Expand(item=self._handle_from_node(node))

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = self._pending_leaves(paths)

        for pending_leaf in result:
            self._append_to_gui(pending_leaf)

        self.expand(self._document_tree.pending_branch)

        return result

    def submit(
            self, reference: JobReference, document_type: Document,
            leaf: AbstractLeaf
    ) -> None:
        reference_label = str(reference)

        if self._document_tree.contains_branch(reference_label):
            self._append_existing(reference_label, document_type, leaf)

        else:
            print("Does not contain reference.")
            job_branch = self._new_job_branch(reference_label)

            document_branch = self._new_document_branch(
                job_branch, document_type)

            document_branch.add(leaf)

            self._remove_from_gui(node=leaf)
            self._append_to_gui(leaf)

        self._gui.ExpandAll()

    def _append_existing(
            self, reference: str, document_type: Document, leaf: AbstractLeaf
    ) -> None:
        job_branch = self._document_tree.branch(reference)

        if job_branch.contains_branch(document_type):
            print(f"Contains {document_type.short_code}")

        else:
            print(f"Does not contain {document_type.short_code}")

    def _on_split_dialog(
            self, dialog: PageRangeDialog, node: AbstractLeaf) -> None:
        option = dialog.ShowModal()

        if option == PageRangeDialog.SPLIT_ALL:
            self._split_all(node)

        elif option == PageRangeDialog.SPLIT_RANGE:
            self._split_range(node, range=dialog.page_range())

    def _split_all(self, node: AbstractNode) -> None:
        for split_node in node.split_all():
            self._append_to_gui(split_node)

    def _split_range(self, node: AbstractNode, range: tuple[int, int]) -> None:
        is_full_range = range == (1, len(node.data))

        if is_full_range:
            return

        self._append_to_gui(node.split_range(start=range[0]-1, stop=range[1]))

    def _new_job_branch(self, reference: str) -> JobBranch:
        result = self._document_tree.create_job_branch(reference)
        self._append_to_gui(result)

        return result

    def _new_document_branch(
            self, job_branch: JobBranch, document_type: Document
    ) -> DocumentBranch:
        result = job_branch.create_branch(document_type=document_type)
        self._append_to_gui(result)

        return result

    def _append_to_gui(self, node: AbstractNode) -> None:
        self._gui.AppendItem(
            parent=self._handle_from_node(node.parent),
            text=node.label,
            data=node.node_id
        )

    def _remove_from_gui(self, node: AbstractNode) -> None:
        self._gui.Delete(self._gui.get_item_handle(node_id=node.node_id))

    def _node_from_handle(self, handle: wx.TreeItemId) -> AbstractNode:
        return self._document_tree.child_by_id(
            node_id=self._gui.get_node_id(tree_handle=handle))

    def _handle_from_node(self, node: AbstractNode) -> wx.TreeItemId:
        return self._gui.get_item_handle(node.node_id)

    def _pending_leaves(self, file_paths: list[str]) -> list[PendingLeaf]:
        return [self._pending_leaf(file_path=path) for path in file_paths]

    def _pending_leaf(self, file_path: str) -> PendingLeaf:
        return PendingLeaf(
            parent=self._document_tree.pending_branch,
            file_name=ntpath.basename(file_path),
            data=rendering.render_images(file_path=file_path)
        )
