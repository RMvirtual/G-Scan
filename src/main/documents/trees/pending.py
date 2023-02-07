from __future__ import annotations

import ntpath
import wx
from src.main.documents.rendering.rendering import render_images
from src.main.documents.trees.interfaces import *


class PendingBranch(AbstractBranch):
    def __init__(self, root: AbstractDocumentRoot) -> None:
        super().__init__(root=root)
