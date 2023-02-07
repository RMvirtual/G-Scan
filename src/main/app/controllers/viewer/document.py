import wx
from src.main import file_system
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main.app.controllers.viewer.tree import DocumentTreeController
from src.main.documents.trees.interfaces import *
from src.main.documents.trees.document import *
from src.main.gui import ImageViewer


class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(gui=self._gui.page_view)
        self._document_tree = DocumentTreeController(gui=self._gui.file_tree)
        self._node_to_view = None

        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self._document_tree.bind_item_selection(self.on_item_selection)

        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_extract_pages(callback=self.on_extract_pages)

    def on_extract_pages(self, event: wx.EVT_BUTTON) -> None:
        print("Extract Pages")

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        selections = self._document_tree.selected_node_ids()

        if selections:
            for selection in selections:
                node = self._document_tree.node_by_id(node_id=selection)
                self._document_tree.remove(node=node)

            self._node_to_view = None
            self._page_view.clear_display()


    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        if not self._node_to_view:
            return

        self._display_node_to_view(page_no=event.Position - 1)

    def on_item_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._document_tree.selected_node_ids()

        if len(selections) == 1:
            self._select_single_document(selections[0])

        elif len(selections) > 1:
            print("Multiple items selected.")

        else:
            print("No items selected apparently.")

    def _select_single_document(self, node_id: wx.TreeItemId) -> None:
        node = self._document_tree.node_by_id(node_id=node_id)

        if not node:
            raise ValueError("No matching node found.")

        if node.is_paperwork_container():
            self._set_node_to_view(node)

    def _set_node_to_view(self, node: AbstractLeaf) -> None:
        self._node_to_view = node
        self._page_view.set_total_pages(len(self._node_to_view.images))
        self._display_node_to_view()

    def _display_node_to_view(self, page_no: int = 0) -> None:
        self._page_view.load_image(self._node_to_view.images[page_no])
        self._page_view.set_page_no(page_no + 1)

    def import_files(self):
        files = file_system.request_files_to_import()

        if files:
            results = self._document_tree.add_pending_files(paths=files)
            self._set_node_to_view(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")
