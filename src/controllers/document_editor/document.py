import wx

from controllers import workflows
from controllers.document_editor.document_tree import DocumentTreeController
from controllers.document_editor.page_view import PageViewController
from data_structures_new import DocumentEntry
from document_tree import DocumentType
from gui.document_editor import Viewer


class DocumentController:
    def __init__(self, gui: Viewer):
        self.gui = gui
        self.page_view = PageViewController(self.gui.page_view)

        self.document_tree = DocumentTreeController(
            self.gui.file_tree.tree_ctrl
        )

        self.page_view.bind_page_no(callback=self.on_page_no_btn)
        self.page_view.bind_delete(callback=self.on_delete_btn)
        self.page_view.bind_split_pages(callback=self.on_split_pages_btn)

        self.gui.file_tree.tree_ctrl.Bind(
            wx.EVT_TREE_SEL_CHANGED, self.on_item_selection
        )

        self.page_view.hide_all_widgets()
        self.current_document: DocumentEntry = None

    def import_files(self):
        # TODO: With this, do we actually need a scan directory??
        files = workflows.request_files()

        if files:
            pending_items = self.document_tree.create_pending_files(files)
            self.view_document_entry(pending_items[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def view_document_entry(self, entry: DocumentEntry) -> None:
        self.current_document = entry

        self.page_view.show_all_widgets()
        self.page_view.set_total_pages(len(self.current_document.pages))

        self.view_page(0)

    def view_page(self, page_no: int) -> None:
        self.page_view.load_image(self.current_document.pages[page_no])
        self.page_view.set_page_no(page_no + 1)

    def clear_view(self) -> None:
        self.current_document = None
        self.page_view.clear_display()

    def assign_current_document(
        self, reference: str, document_type: DocumentType
    ) -> None:
        self.document_tree.move_entry(
            self.current_document, reference, document_type
        )

        self.document_tree.create_job_node(
            reference, document_type, leaf=self.current_document
        )

    def on_split_pages_btn(self, event: wx.Event) -> None:
        self.document_tree.split_pages(self.current_document)

    def on_page_no_btn(self, event: wx.Event) -> None:
        self.view_page(page_no=event.Position - 1)

    def on_delete_btn(self, event: wx.Event) -> None:
        self.document_tree.delete_selected()
        self.page_view.clear_display()

    def on_item_selection(self, event: wx.Event) -> None:
        selections = self.document_tree.selected_items()

        if len(selections) == 1:
            node = selections[0]

            if node.is_leaf():
                self.view_document_entry(node)

            elif node.is_branch():
                self.document_tree.expand(node)
                self.page_view.hide_all_widgets()
                self.clear_view()

        elif len(selections) > 1:
            self.page_view.hide_split_button()

        else:
            self.page_view.hide_all_widgets()
            self.clear_view()
