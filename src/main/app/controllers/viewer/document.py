import wx
from src.main import file_system
from src.main.app.controllers.viewer.page_view import PageViewController
from src.main.app.controllers.viewer.tree import DocumentTreeController
from src.main.documents.trees.interfaces import *
from src.main.documents.trees.document import *
from src.main.gui import ImageViewer
from src.main.gui.dialogs.document_split import DocumentSplitDialog


class DocumentController:
    def __init__(self, gui: ImageViewer):
        self._gui = gui
        self._page_view = PageViewController(gui=self._gui.page_view)
        self._document_tree = DocumentTreeController(gui=self._gui.file_tree)
        self._page_view.hide_all_widgets()
        self._bind_callbacks()

    def _bind_callbacks(self) -> None:
        self._document_tree.bind_item_selection(self.on_item_selection)

        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_extract_pages(callback=self.on_extract_pages)

    def import_files(self):
        files = file_system.file_import_dialog()

        if files:
            results = self._document_tree.add_pending_files(paths=files)
            self._set_node_to_view(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def on_extract_pages(self, event: wx.EVT_BUTTON) -> None:
        with DocumentSplitDialog(5) as dialog:
            option = dialog.ShowModal()

            if option == DocumentSplitDialog.SPLIT_ALL:
                print("Split All")

            elif option == DocumentSplitDialog.SPLIT_RANGE:
                range = dialog.page_range()
                print("Split Range")
                print(range)

            elif option == DocumentSplitDialog.CANCEL:
                print("Cancel")

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
        selections = self._document_tree.selected_node_ids()

        if len(selections) == 1:
            print("One item selected.")
            node = self._document_tree.node_by_id(node_id=selections[0])

            if node.is_leaf():
                self._set_node_to_view(node)

            elif node.is_branch():
                self._clear_node_to_view()

        elif len(selections) > 1:
            print("Multiple items selected.")
            self._page_view.hide_split_button()

        else:
            print("No items selected apparently.")
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _set_node_to_view(self, node: AbstractLeaf) -> None:
        self._page_view.show_all_widgets()
        self._currently_viewed = node
        self._page_view.show_all_widgets()
        self._page_view.set_total_pages(len(self._currently_viewed.data))
        self._display_node_to_view()

    def _clear_node_to_view(self) -> None:
        self._currently_viewed = None
        self._page_view.clear_display()

    def _display_node_to_view(self, page_no: int = 0) -> None:
        self._page_view.load_image(self._currently_viewed.data[page_no])
        self._page_view.set_page_no(page_no + 1)
