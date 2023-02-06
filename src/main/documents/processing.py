import wx


class PendingDocuments:
    def __init__(self, tree: wx.TreeCtrl):
        self.tree = tree
        self.pending_files = []

        self.tree_head = self.tree.AppendItem(
            parent=self.tree.GetRootItem(), text="Pending Items")

    def update_item_count(self) -> None:
        self.tree.SetItemText(
            item=self.tree_head,
            text=f"Pending Items ({len(self.pending_files)})"
        )

    def add_file(self, file_name: str) -> None:
        self.pending_files.append(file_name)
        self.update_item_count()


class PendingDocument:
    def __init__(self):
        self.tree_item = wx.TreeItemId()
        self.file_name = ""

    def number_of_pages(self) -> None:
        ...


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

