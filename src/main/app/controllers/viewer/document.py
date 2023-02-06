import wx
from src.main.documents.trees.interfaces import AbstractNode
from src.main.documents.trees.pending import PendingTree
from src.main.documents.trees import TreeRoot
from src.main.gui import ImageViewer
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main import file_system


class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(page_canvas=self._gui.page_view)
        self._initialise_document_trees()
        self._bind_callbacks()
        self._node_to_view = None

    def _initialise_document_trees(self) -> None:
        self.tree_root = TreeRoot(tree_control=self._gui.file_tree.tree)
        self.pending_tree = PendingTree(absolute_root=self.tree_root)

    def _bind_callbacks(self) -> None:
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED, handler=self.on_file_tree_selection)

        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_extract_pages(callback=self.on_extract_pages)

    def on_extract_pages(self, event: wx.EVT_BUTTON) -> None:
        print("Extract Pages")

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        print("Delete")

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        if not self._node_to_view:
            return

        self._display_node_to_view(page_no=event.Position - 1)

    def on_file_tree_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if len(selections) == 1:
            self.select_single_document(selections[0])

        elif len(selections) > 1:
            print("Multiple items selected.")

        else:
            print("No items selected apparently.")

    def select_single_document(self, node_id: wx.TreeItemId) -> None:
        node = self.pending_tree.find_node(node_id=node_id)

        if not node:
            raise ValueError("No matching node found.")

        if node.is_leaf_node():
            self._set_node_to_view(node)

    def _set_node_to_view(self, node: AbstractNode) -> None:
        self._node_to_view = node
        self._page_view.set_total_pages(len(self._node_to_view.images))
        self._display_node_to_view()

    def _display_node_to_view(self, page_no: int = 0) -> None:
        self._page_view.load_image(self._node_to_view.images[page_no])
        self._page_view.panel.page_no.SetValue(page_no + 1)

    def import_files(self):
        files = file_system.request_files_to_import()

        if files:
            results = self.pending_tree.add_files(paths=files)
            self._set_node_to_view(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")
