from pathlib import Path

import wx
from wx import TreeCtrl

import rendering
from data_structures import AbstractLeaf, AbstractNode
from data_structures_new import (
    Branch,
    DocumentEntry,
    DocumentTree,
    DocumentTypeBranch,
    JobBranch,
)
from document_tree import DocumentBranch, PendingLeaf
from documents import DocumentType
from gui.page_range_dialog import PageRangeDialog


class DocumentTreeController:
    def __init__(self, gui: TreeCtrl) -> None:
        self.tree = DocumentTree()
        self.gui = gui
        self.gui.AddRoot(text="Document Tree", data=id(self.tree))

        # Create pending branch.
        pending_id = self.gui.AppendItem(
            parent=self.gui.GetRootItem(),
            text="Pending",
            data=self.tree.pending,
        )

        self.tree.pending.gui_id = pending_id

    def create_pending_files(self, paths: list[str]) -> list[DocumentEntry]:
        branch = self.tree.pending
        result = []

        for path in paths:
            entry = branch.create_document_entry(Path(path).name, None)
            entry.pages = rendering.load_images(path)

            entry.gui_id = self.gui.AppendItem(
                parent=branch.gui_id, text=entry.name, data=entry
            )

            result.append(entry)

        self.gui.Expand(branch.gui_id)

        return result

    def split_pages(self, node: AbstractLeaf) -> None:
        with PageRangeDialog(max_pages=len(node.data)) as dialog:
            self._on_split_dialog(dialog, node)

    def delete_current(self) -> None:
        gui_ids = self.gui.GetSelections()

        for gui_id in gui_ids:
            entry = self.gui.GetItemData(gui_id)
            self.delete(entry)

    def delete(self, entry: JobBranch | DocumentEntry) -> None:
        if isinstance(entry, JobBranch):
            self.tree.remove(entry)
            self.gui.Delete(entry.gui_id)
            entry.gui_id = None

        elif isinstance(entry, DocumentEntry):
            entry.parent.remove(entry)
            self.gui.Delete(entry.gui_id)
            entry.gui_id = None

    def create_job_node(
        self,
        reference: str,
        document_type: DocumentType,
        leaf: AbstractLeaf,
    ) -> None:
        reference_label = reference

        if self.tree.contains_branch(reference_label):
            self._append_existing(reference_label, document_type, leaf)

        else:
            job_branch = self._new_job_branch(reference_label)

            document_branch = self._new_document_branch(
                job_branch, document_type
            )

            document_branch.add(leaf)

            self._remove_from_gui(node=leaf)
            self._append_to_gui(leaf)

        self.gui.ExpandAll()

    def move_entry(
        self, entry: DocumentEntry, reference: str, document_type: DocumentType
    ) -> None:
        self.gui.Delete(self.tree_handle(entry))
        job_branch = self.tree.create_job_branch(reference)
        job_branch.append(entry)

        self.gui.AppendItem(
            parent=self._handle_from_node(entry.parent),
            text=node.label,
            data=node.node_id,
        )

        return None

    def _append_existing(
        self, reference: str, document_type: DocumentType, leaf: AbstractLeaf
    ) -> None:
        job_branch = self.tree.branch(reference)

        if job_branch.contains_branch(document_type):
            print(f"Contains {document_type.short_code}")

        else:
            print(f"Does not contain {document_type.short_code}")

    def _on_split_dialog(
        self, dialog: PageRangeDialog, node: AbstractLeaf
    ) -> None:
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

        self._append_to_gui(
            node.split_range(start=range[0] - 1, stop=range[1])
        )

    def _new_job_branch(self, reference: str) -> JobBranch:
        result = self.tree.create_job_branch(reference)
        self._append_to_gui(result)

        return result

    def _new_document_branch(
        self, job_branch: JobBranch, document_type: DocumentType
    ) -> DocumentBranch:
        result = job_branch.create_branch(document_type=document_type)
        self._append_to_gui(result)

        return result

    def _append_to_gui(self, node: AbstractNode) -> None:
        self.gui.AppendItem(
            parent=self._handle_from_node(node.parent),
            text=node.label,
            data=node.node_id,
        )

    def _remove_from_gui(self, node: AbstractNode) -> None:
        self.gui.Delete(self._handle_from_node(node))

    def tree_handle(self, item_id) -> wx.TreeItemId:
        root_handle = self.gui.GetRootItem()

        if self.gui.GetItemData(item=root_handle) == item_id:
            return root_handle

        item, cookie = self.gui.GetFirstChild(item=root_handle)

        while item.IsOk():
            data = self.gui.GetItemData(item)

            if data == item_id:
                return item

            if self.gui.ItemHasChildren(item):
                match = self._find_child_handle(node_id=item_id, root_id=item)

                if match.IsOk():
                    return match

            item, cookie = self.gui.GetNextChild(root_handle, cookie)

        child = wx.TreeItemId()

        if not child.IsOk():
            raise ValueError(f"Node ID {item_id} does not exist in tree.")

        return child

    def _handle_from_node(self, node: AbstractNode) -> wx.TreeItemId:
        root_handle = self.gui.GetRootItem()

        if self.gui.GetItemData(item=root_handle) == node.node_id:
            return root_handle

        child = self._find_child_handle(
            node_id=node.node_id, root_id=root_handle
        )

        if not child.IsOk():
            raise ValueError(f"Node ID {node.node_id} does not exist in tree.")

        return child

    def _find_child_handle(
        self, node_id: int, root_id: wx.TreeItemId
    ) -> wx.TreeItemId:
        item, cookie = self.gui.GetFirstChild(item=root_id)

        while item.IsOk():
            data = self.gui.GetItemData(item)

            if data == node_id:
                return item

            if self.gui.ItemHasChildren(item):
                match = self._find_child_handle(node_id=node_id, root_id=item)

                if match.IsOk():
                    return match

            item, cookie = self.gui.GetNextChild(root_id, cookie)

        return wx.TreeItemId()
