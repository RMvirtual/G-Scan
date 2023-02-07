import wx
from src.main.gui.image_viewer.panels import DocumentTreeView
from src.main.documents.trees import DocumentTree


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeView):
        self.gui = gui
        self.document_tree = DocumentTree(tree_control=self.gui.tree)

    def selected_items(self) -> list[wx.TreeItemId]:
        return self._gui.tree.GetSelections()

    def node_by_id(self, node_id) -> any:
        return self.document_tree.find_node_by_id(node_id=node_id)

    def bind_item_selection(self, callback) -> None:
        self.gui.tree.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)

    def add_pending(self, paths: list[str]) -> None:
        print(paths)
