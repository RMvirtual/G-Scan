import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class DocumentRoot(AbstractNode):
    def __init__(self, tree_control: wx.TreeCtrl, text: str):
        super().__init__(parent=None)
        self.tree_control = tree_control

        self.node_id = self.tree_control.AppendItem(
            parent=tree_control.GetRootItem(), text=text)

    def is_root(self) -> bool:
        return True

    def is_child_node(self) -> bool:
        return False

    def append_child(self) -> AbstractNode:
        ...


class DocumentNode(AbstractNode):
    def __init__(self, parent_node: AbstractNode):
        super().__init__(parent=parent_node)
        self.parent_node = parent_node

    def is_root(self) -> bool:
        return False

    def is_child_node(self) -> bool:
        return self.parent_node is not None


class JobReferenceNode(DocumentRoot):
    def __init__(self, tree_control: wx.TreeCtrl, reference: str):
        super().__init__(tree_control, reference)
        self.reference = reference


class PaperworkNode(DocumentNode):
    def __init__(self, parent_node: JobReferenceNode):
        super().__init__(parent_node)


class DocumentLeaf(DocumentNode):
    def __init__(self, parent_node) -> None:
        super().__init__(parent_node)


class ProcessedTree:
    def __init__(self) -> None:
        ...
