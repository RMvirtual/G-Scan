import wx
from src.main.documents.trees.pending import *
from src.main.documents.trees.interfaces import *


class DocumentTree(AbstractDocumentRoot):
    """Requires a wx.TreeCtrl object to plug into to create the node
    references.
    """
    def __init__(self, tree_control: wx.TreeCtrl) -> None:
        super().__init__(tree_control=tree_control)

        self.pending_branch = PendingBranch(parent=self)
        self.processed_branches = []
