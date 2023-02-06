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
        self.refresh_count()

        return result

    def refresh_count(self) -> None:
        self.tree.SetItemText(
            item=self.pending_category,
            text=f"Pending Items ({len(self.pending)})"
        )

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

