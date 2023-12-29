import wx
import file_system

from controllers.abstract_root import RootInterface
from controllers.configuration import AppConfiguration
from controllers.document_tree import DocumentTreeController
from controllers.page_view import PageViewController
from controllers.user_input import SubmissionDocument, UserInputController
from data_structures import AbstractNode
from document_tree import PendingLeaf
from views import Viewer


class DocumentController:
    def __init__(self, gui: Viewer):
        self._gui = gui
        self._page_view = PageViewController(self._gui.page_view)
        self._document_tree = DocumentTreeController(self._gui.file_tree.tree)
        self._bind_callbacks()

        self._page_view.hide_all_widgets()
        self._currently_viewed = None

    def _bind_callbacks(self) -> None:
        self._page_view.bind_page_no(callback=self.on_page_no)
        self._page_view.bind_delete(callback=self.on_delete)
        self._page_view.bind_split_pages(callback=self.on_split_pages)
        self._document_tree.bind_selection(callback=self.on_item_selection)

    def import_files(self):
        files = file_system.file_import_dialog()

        if files:
            results = self.add_pending_files(paths=files)
            self._set_currently_viewed(results[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def submit(self, submission: SubmissionDocument) -> None:
        self._document_tree.create_job_node(
            reference=submission.reference,
            document_type=submission.document_type,
            leaf=self._currently_viewed
        )

    def on_split_pages(self, event: wx.EVT_BUTTON) -> None:
        self._document_tree.split_pages(self._currently_viewed)

    def on_delete(self, event: wx.EVT_BUTTON) -> None:
        self._document_tree.delete_selected()
        self._page_view.clear_display()

    def on_page_no(self, event: wx.EVT_SPINCTRL) -> None:
        self._display_node_to_view(page_no=event.Position - 1)

    def on_item_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._document_tree.selected_items()

        if len(selections) == 1:
            self._on_single_item_selection(node=selections[0])

        elif len(selections) > 1:
            self._on_multiple_item_selections(nodes=selections)

        else:
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _on_single_item_selection(self, node: AbstractNode) -> None:
        if node.is_leaf():
            self._set_currently_viewed(node)

        elif node.is_branch():
            self._document_tree.expand(node)
            self._page_view.hide_all_widgets()
            self._clear_node_to_view()

    def _on_multiple_item_selections(self, nodes: list[AbstractNode]) -> None:
        self._page_view.hide_split_button()

    def _set_currently_viewed(self, node: AbstractNode) -> None:
        if not node.is_leaf():
            raise ValueError("Node is not viewable leaf.")

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

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        return self._document_tree.add_pending_files(paths)


class DocumentEditorController:
    def __init__(
            self, root_application: RootInterface, config: AppConfiguration
    ) -> None:
        
        self._root = root_application
        self._config = config

        self._gui = Viewer(self._root.window)
        self._root.window.set_panel(self._gui)

        file_menu = self._gui.file_menu

        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_files,
            source=file_menu.import_files
        )

        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_as,
            source=file_menu.import_prenamed_files
        )

        self._root.window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)

        self._gui.input_bar.submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._documents = DocumentController(self._gui)
        self._user_input = UserInputController(self._gui, self._config)

    def on_submit(self, _event: wx.EVT_BUTTON) -> None:
        submission_document = self._user_input.submission_document()

        if submission_document.reference:
            self._documents.submit(submission_document)

    def on_import_files(self, event: wx.EVT_MENU) -> None:
        self._documents.import_files()

    def on_import_as(self, event: wx.EVT_MENU) -> None:
        self._documents.import_as()

    def on_quit(self, event: wx.EVT_MENU = None) -> None:
        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event = None) -> None:
        self._gui.Destroy()
        self._root.window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

