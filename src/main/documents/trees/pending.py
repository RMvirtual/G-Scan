import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class PendingBranch(AbstractBranch):
    def __init__(self, parent: AbstractDocumentRoot) -> None:
        super().__init__(parent=parent, label="Pending")


class PendingLeaf(AbstractLeaf):
    def __init__(self, parent: PendingBranch, file_name: str = "") -> None:
        super().__init__(parent=parent, label=file_name)
