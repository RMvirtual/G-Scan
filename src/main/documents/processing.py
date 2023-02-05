import wx


class DocumentToProcess:
    def __init__(self):
        self.file_path = ""
        self.parent_item_id = wx.TreeItemId()
        self.tree_item_id = wx.TreeItemId()


class DocumentWorkload:
    def __init__(self):
        self.pending: list[DocumentToProcess] = []
        self.processed: list[DocumentToProcess] = []
