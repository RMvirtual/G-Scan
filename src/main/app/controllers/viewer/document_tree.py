import ntpath
import wx
from src.main.data_structures import *

from src.main.documents import (
    Document, DocumentBranch, DocumentLeaf, DocumentTree, JobBranch,
    PendingBranch, PendingLeaf, rendering
)

from src.main.gui.dialogs.document_split import DocumentSplitDialog
from src.main.gui.viewer.document_tree import DocumentTreeCtrl


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeCtrl):
        self._gui = gui
        self._document_tree = DocumentTree()

        root = self._document_tree.root
        self._gui.AddRoot(text=root.label, data=root.node_id)

        self.append_to_gui(self._document_tree.root.pending_branch)

    def bind_selection(self, callback) -> None:
        self._gui.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)
        # self._gui.Bind(event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = self.pending_leaves_from_files(paths)

        for pending_leaf in result:
            self.append_to_gui(pending_leaf)

        self.expand(self._document_tree.pending_branch)

        return result

    def pending_leaves_from_files(self, paths: list[str]) -> list[PendingLeaf]:
        return [self._create_pending_leaf(file_path=path) for path in paths]

    def submit(
            self, reference: str, document_type: Document,
            leaf: AbstractLeaf
    ) -> None:
        if self._document_tree.contains_branch(reference):
            self._append_existing(reference, document_type, leaf)

        else:
            print("Does not contain reference.")
            job_branch = self._new_job_branch(reference)

            document_branch = self._new_document_branch(
                job_branch, document_type)

            document_branch.add(leaf)

            self.remove_from_gui(node=leaf)
            self.append_to_gui(leaf)

        self._gui.ExpandAll()

    def remove_from_gui(self, node: AbstractNode) -> None:
        self._gui.Delete(self._gui.get_item_handle(node_id=node.node_id))

    def _append_existing(
            self, reference: str, document_type: Document, leaf: AbstractLeaf
    ) -> None:
        job_branch = self._document_tree.branch(reference)

        if job_branch.contains_branch(document_type):
            print(f"Contains {document_type.short_code}")

        else:
            print(f"Does not contain {document_type.short_code}")

    def _root_tree_handle(self) -> wx.TreeItemId:
        return self._handle_from_node(self._document_tree.root)

    def _node_from_handle(self, handle: wx.TreeItemId) -> AbstractNode:
        node_id = self._gui.get_node_id(tree_handle=handle)

        return self._document_tree.child_by_id(node_id=node_id)

    def _handle_from_node(self, node: AbstractNode) -> wx.TreeItemId:
        return self._gui.get_item_handle(node.node_id)

    def _new_document_branch(
            self, job_branch: JobBranch, document_type: Document
    ) -> DocumentBranch:
        result = job_branch.create_branch(document_type=document_type)
        self.append_to_gui(result)

        return result

    def append_to_gui(self, node: AbstractNode) -> None:
        self._gui.AppendItem(
            parent=self._handle_from_node(node.parent),
            text=node.label,
            data=node.node_id
        )

    def _new_job_branch(self, reference: str) -> JobBranch:
        result = self._document_tree.create_job_branch(reference)
        self.append_to_gui(result)

        return result

    def _create_pending_leaf(self, file_path: str) -> PendingLeaf:
        return PendingLeaf(
            parent=self._document_tree.pending_branch,
            file_name=ntpath.basename(file_path),
            data=rendering.render_images(file_path=file_path)
        )

    def selected_items(self) -> list[AbstractNode]:
        return [
            self._node_from_handle(handle=selection)
            for selection in self._gui.GetSelections()
            if selection is not None
        ]

    def split_pages(self, node: AbstractLeaf) -> None:
        with DocumentSplitDialog(len(node.data)) as dialog:
            option = dialog.ShowModal()

            if option == DocumentSplitDialog.SPLIT_ALL:
                node.split_all()

            elif option == DocumentSplitDialog.SPLIT_RANGE:
                range = dialog.page_range()
                node.split_range(start=range[0] - 1, stop=range[1])

    def delete_selected(self) -> None:
        for node in self.selected_items():
            node.detach()
            self._gui.Delete(item=self._handle_from_node(node))

    def expand(self, node: AbstractNode) -> None:
        tree_handle = self._gui.get_item_handle(node_id=node.node_id)
        self._gui.Expand(item=tree_handle)
