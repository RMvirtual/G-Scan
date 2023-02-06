import wx
from src.main.documents.rendering import render_images


class PendingDocument:
    def __init__(self, file_path: str):
        self.original_path = file_path
        self.file_name = ""
        self.tree_item = wx.TreeItemId()
        self.images = render_images(self.original_path)

    def __len__(self) -> int:
        return len(self.images)


class PendingDocuments:
    def __init__(self, tree: wx.TreeCtrl):
        self.tree = tree
        self.pending: list[PendingDocument] = []

        self.tree_head = self.tree.AppendItem(
            parent=self.tree.GetRootItem(), text="")

    def __len__(self) -> int:
        return len(self.pending)

    def __getitem__(self, index: int) -> PendingDocument:
        return self.pending[index]

    def add_file(self, file_path: str) -> None:
        self.pending.append(PendingDocument(file_path=file_path))
        self.refresh_count()

    def refresh_count(self) -> None:
        self.tree.SetItemText(
            item=self.tree_head,
            text=f"Pending Items ({len(self.pending)})"
        )

    def head_document(self) -> PendingDocument:
        return self.pending[0] if self.pending else None

    def tail_document(self) -> PendingDocument:
        return self.pending[-1] if self.pending else None


class ProcessedDocuments:
    def __init__(self):
        ...

class DocumentToProcess:
    def __init__(self):
        self.file_path = ""
        self.parent_item_id = wx.TreeItemId()
        self.tree_item_id = wx.TreeItemId()


class DocumentWorkload:
    def __init__(self):
        self.pending: list[DocumentToProcess] = []
        self.processed: list[DocumentToProcess] = []

