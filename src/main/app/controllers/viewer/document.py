import wx
from src.main import file_system
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main.documents.trees.interfaces import *
from src.main.documents.trees.document import *
from src.main.documents.trees.pending import *
from src.main.gui import ImageViewer
from src.main.gui.dialogs.document_split import DocumentSplitDialog
from src.main.documents import Document
from src.main.gui.image_viewer.panels import DocumentTreeView
from src.main.documents.trees import DocumentTree
from src.main.documents.trees.pending import PendingLeaf
from src.main.documents.rendering import rendering
from src.main.documents.trees.interfaces import AbstractNode

class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(gui=self._gui.page_view)
        self._document_tree = DocumentTree(
            tree_control=self._gui.file_tree.tree)
        self._page_view.hide_all_widgets()
        self._currently_viewed = None
        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self.bind_item_selection(self.on_item_selection)

        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_extract_pages(callback=self.on_split_pages)

    def import_files(self):
        files = file_system.file_import_dialog()

        if files:
            results = self.add_pending_files(paths=files)
            self._set_currently_viewed(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def submit_selection(
            self, job_reference: str, document_type: Document) -> None:
        if self._document_tree.contains_branch(job_reference):
            print("Contains reference.")

        else:
            print("Does not contain reference.")

    def on_split_pages(self, event: wx.EVT_BUTTON) -> None:
        with DocumentSplitDialog(len(self._currently_viewed.data)) as dialog:
            option = dialog.ShowModal()

            if option == DocumentSplitDialog.SPLIT_ALL:
                self._currently_viewed.split_all()

            elif option == DocumentSplitDialog.SPLIT_RANGE:
                range = dialog.page_range()
                self._currently_viewed.split_range(
                    start=range[0] - 1, stop=range[1])

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        selections = self._document_tree.selected_node_ids()

        if selections:
            for selection in selections:
                node = self._document_tree.node_by_id(node_id=selection)
                self._document_tree.remove(node=node)

            self._page_view.clear_display()

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        self._display_node_to_view(page_no=event.Position - 1)

    def on_item_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self.selected_node_ids()

        if len(selections) == 1:
            print("One item selected.")
            node = self._document_tree.find_node_by_id(node_id=selections[0])

            if node.is_leaf():
                self._set_currently_viewed(node)

            elif node.is_branch():
                self._page_view.hide_all_widgets()
                self._clear_node_to_view()

        elif len(selections) > 1:
            print("Multiple items selected.")
            self._page_view.hide_split_button()

        else:
            print("No items selected apparently.")
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _set_currently_viewed(self, node: AbstractLeaf) -> None:
        if not node.is_leaf():
            raise ValueError("Node is not viewable leaf.")

        self._currently_viewed = node

        self._page_view.show_all_widgets()
        self._page_view.show_all_widgets()
        self._page_view.set_total_pages(len(self._currently_viewed.data))

        self._display_node_to_view()

    def _clear_node_to_view(self) -> None:
        self._currently_viewed = None
        self._page_view.clear_display()

    def _display_node_to_view(self, page_no: int = 0) -> None:
        self._page_view.load_image(self._currently_viewed.data[page_no])
        self._page_view.set_page_no(page_no + 1)

    ##########################################################
    def selected_node_ids(self) -> list[wx.TreeItemId]:
        return self._gui.file_tree.tree.GetSelections()

    def node_by_id(self, node_id) -> any:
        return self._document_tree.find_node_by_id(node_id=node_id)

    def bind_item_selection(self, callback) -> None:
        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED, handler=callback)

        self._gui.file_tree.tree.Bind(
            event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = []

        for path in paths:
            new_item = PendingLeaf(
                parent=self._document_tree.pending_branch, file_name=path)

            new_item.data = rendering.render_images(file_path=path)
            result.append(new_item)

        self._gui.file_tree.tree.ExpandAll()

        return result

    def remove(self, node: AbstractNode) -> None:
        self._document_tree.remove(node=node)
