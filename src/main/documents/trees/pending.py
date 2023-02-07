from __future__ import annotations
import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class PendingBranch(AbstractBranch):
    def __init__(self, root: AbstractDocumentRoot) -> None:
        super().__init__(root=root, label="Pending")

    def is_paperwork_container(self) -> bool:
        return False


class PendingLeaf(AbstractLeaf):
    def __init__(self, parent: PendingBranch, label: str = "") -> None:
        super().__init__(parent=parent, label=label)

