import ntpath
import wx
from src.main.documents.rendering import render_images

class PendingDocument:
    def __init__(self, file_path: str):
        self.file_name = ntpath.basename(file_path)
        self.tree_item = wx.TreeItemId()
        self.images = render_images(file_path)

    def __len__(self) -> int:
        return len(self.images)


class PendingDocuments:
    def __init__(self, tree: wx.TreeCtrl):
        self.tree = tree
        self.pending: list[PendingDocument] = []

        self.pending_category: wx.TreeItemId = self.tree.AppendItem(
            parent=self.tree.GetRootItem(), text="")

    def add_pending(self, file_path: str) -> PendingDocument:
        result = PendingDocument(file_path=file_path)

        result.tree_item = self.tree.AppendItem(
            parent=self.pending_category,
            text=f"{result.file_name} ({len(result)})"
        )

        self.tree.Expand(self.pending_category)
        self.pending.append(result)

        return result

    def head_document(self) -> PendingDocument:
        return self.pending[0] if self.pending else None

    def tail_document(self) -> PendingDocument:
        return self.pending[-1] if self.pending else None

    def from_file_name(self, file_name: str) -> PendingDocument:
        matching_items = filter(
            lambda x: x.file_name == file_name, self.pending)

        return next(matching_items)

    def __len__(self) -> int:
        return len(self.pending)

    def __getitem__(self, index: int) -> PendingDocument:
        return self.pending[index]



class DocumentTree:
    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        self.tree_control = tree_control
        self.root_id = self.tree_control.AddRoot(text="All Files")

        self.pending_root = self.tree_control.AppendItem(
            parent=self.root_id, text="Pending")

        self.tree_control.ExpandAll()

    def add_pending(self, file_path: str) -> PendingDocument:
        result = PendingDocument(file_path=file_path)

        result.tree_item = self.tree_control.AppendItem(
            parent=self.pending_root,
            text=f"{result.file_name} ({len(result)})"
        )

        self.tree_control.Expand(self.pending_root)
        # self.pending.append(result)

        return result

    def _refresh_count(self) -> None:
        self.tree_control.SetItemText(
            item=self.pending_root,
            text=f"Pending Items ({len(self.pending)})"
        )


