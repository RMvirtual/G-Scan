import wx
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
        self._current_node = None

    def _initialise_document_trees(self) -> None:
        self.tree_root = TreeRoot(tree_control=self._gui.file_tree.tree)
        self.pending_tree = PendingTree(absolute_root=self.tree_root)

    def _bind_callbacks(self) -> None:
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED,
            handler=self.on_file_tree_selection
        )

        self._bind_page_view_callbacks()

    def _bind_page_view_callbacks(self) -> None:
        self._page_view.panel.page_no.Bind(
            event=wx.EVT_SPINCTRL, handler=self.on_page_no)

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        print(f"Page Number event: {event.Position}.")
        self._page_view.load_image(
            self._current_node.images[event.Position - 1])

    def on_file_tree_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if len(selections) == 1:
            item = selections[0]

            node = self.pending_tree.find_node(node_id=item)

            if not node:
                raise ValueError("No matching node found.")

            if node.is_leaf_node():
                self._current_node = node
                self.set_document()

        elif len(selections) > 1:
            print("Multiple items selected.")

        else:
            print("No items selected apparently.")

    def set_document(self) -> None:
        self._page_view.load_image(self._current_node.images[0])
        self._page_view.set_total_pages(len(self._current_node.images))
        self._page_view.panel.page_no.SetValue(1)

    def import_files(self):
        files = file_system.request_files_to_import()

        if files:
            results = self.pending_tree.add_files(paths=files)
            self._page_view.load_image(results[0].images[0])

    def import_as(self) -> None:
        print("Michelin Mode")
