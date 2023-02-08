import wx
from src.main.gui.image_viewer.panels import DocumentTreeView
from src.main.documents.trees import DocumentTree
from src.main.documents.trees.pending import PendingLeaf
from src.main.documents.rendering import rendering
from src.main.documents.trees.interfaces import AbstractNode


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeView):
        self._gui = gui
        self._document_tree = DocumentTree(tree_control=self._gui.tree)

    def selected_node_ids(self) -> list[wx.TreeItemId]:
        return self._gui.tree.GetSelections()

    def node_by_id(self, node_id) -> any:
        return self._document_tree.find_node_by_id(node_id=node_id)

    def bind_item_selection(self, callback) -> None:
        self._gui.tree.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)

        self._gui.tree.Bind(
            event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)


    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = []

        for path in paths:
            new_item = PendingLeaf(
                parent=self._document_tree.pending_branch, file_name=path)

            new_item.data = rendering.render_images(file_path=path)
            result.append(new_item)

        self._gui.tree.ExpandAll()

        return result

    def remove(self, node: AbstractNode) -> None:
        self._document_tree.remove(node=node)
