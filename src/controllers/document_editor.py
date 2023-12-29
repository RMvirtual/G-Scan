import wx
import ntpath
import file_system
import rendering

from wx.lib.floatcanvas import FloatCanvas
from configuration import AppConfiguration, RootInterface
from data_structures import AbstractNode, AbstractLeaf
from document_tree import DocumentBranch, DocumentTree, JobBranch, PendingLeaf
from document_type import DocumentType
from job_references import JobReference
from views import Viewer
from views.page_range_dialog import PageRangeDialog
from views.document_editor.document_tree import DocumentTreeCtrl
from views.document_editor.panels import PageView
from views.window import Window


class SubmissionDocument:
    def __init__(self, reference: JobReference, document_type: DocumentType):
        self.reference = reference
        self.document_type = document_type


class UserInputController:
    def __init__(self, gui: Viewer, config: AppConfiguration) -> None:
        self._gui = gui
        self._config = config

        self._input_bar = self._gui.input_bar

        departments = list(map(
            lambda dept: dept.full_name, self._config.departments))
        
        self._input_bar.department_options = departments

        current_department = self._config.department.full_name
        self._input_bar.department = current_department

        documents = list(map(
            lambda d: d.full_name, self._config.department.document_types))

        self._input_bar.document_options = documents

        current_document = self._config.document_type.full_name
        self._input_bar.document_type = current_document

    def submission_document(self) -> SubmissionDocument:
        return SubmissionDocument(self.job_reference(), self.document_type())

    def job_reference(self) -> JobReference or None:
        reference = self._input_bar.reference_input

        try:
            return JobReference(reference)

        except ValueError:
            message_box = wx.MessageDialog(
                parent=None, message=f"Job reference {reference} is invalid.",
                caption="Invalid Job Reference"
            )

            with message_box:
                message_box.ShowModal()

            return None

    def document_type(self) -> DocumentType:
        return self._config.database.document(
            full_name=self._input_bar.document_type)


class DocumentTreeController:
    def __init__(self, gui: DocumentTreeCtrl):
        self._gui = gui
        self._document_tree = DocumentTree()
        self._initialise_root_node()
        self._append_to_gui(self._document_tree.root.pending_branch)

    def _initialise_root_node(self) -> None:
        root = self._document_tree.root
        self._gui.AddRoot(text=root.label, data=root.node_id)

    def bind_selection(self, callback) -> None:
        self._gui.Bind(event=wx.EVT_TREE_SEL_CHANGED, handler=callback)
        # self._gui.Bind(event=wx.EVT_TREE_ITEM_ACTIVATED, handler=callback)

    def selected_items(self) -> list[AbstractNode]:
        return [
            self._node_from_handle(handle=selection)
            for selection in self._gui.GetSelections() if selection is not None
        ]

    def split_pages(self, node: AbstractLeaf) -> None:
        with PageRangeDialog(max_pages=len(node.data)) as dialog:
            self._on_split_dialog(dialog, node)

    def delete_selected(self) -> None:
        for node in self.selected_items():
            node.detach()
            self._remove_from_gui(node)

    def expand(self, node: AbstractNode) -> None:
        self._gui.Expand(item=self._handle_from_node(node))

    def add_pending_files(self, paths: list[str]) -> list[PendingLeaf]:
        result = self._pending_leaves(paths)

        for pending_leaf in result:
            self._append_to_gui(pending_leaf)

        self.expand(self._document_tree.pending_branch)

        return result

    def create_job_node(
            self, reference: JobReference, document_type: DocumentType,
            leaf: AbstractLeaf
    ) -> None:
        reference_label = str(reference)

        if self._document_tree.contains_branch(reference_label):
            self._append_existing(reference_label, document_type, leaf)

        else:
            job_branch = self._new_job_branch(reference_label)

            document_branch = self._new_document_branch(
                job_branch, document_type)

            document_branch.add(leaf)

            self._remove_from_gui(node=leaf)
            self._append_to_gui(leaf)

        self._gui.ExpandAll()

    def _append_existing(
            self, reference: str, document_type: DocumentType, leaf: AbstractLeaf
    ) -> None:
        job_branch = self._document_tree.branch(reference)

        if job_branch.contains_branch(document_type):
            print(f"Contains {document_type.short_code}")

        else:
            print(f"Does not contain {document_type.short_code}")

    def _on_split_dialog(
            self, dialog: PageRangeDialog, node: AbstractLeaf) -> None:
        option = dialog.ShowModal()

        if option == PageRangeDialog.SPLIT_ALL:
            self._split_all(node)

        elif option == PageRangeDialog.SPLIT_RANGE:
            self._split_range(node, range=dialog.page_range())

    def _split_all(self, node: AbstractNode) -> None:
        for split_node in node.split_all():
            self._append_to_gui(split_node)

    def _split_range(self, node: AbstractNode, range: tuple[int, int]) -> None:
        is_full_range = range == (1, len(node.data))

        if is_full_range:
            return

        self._append_to_gui(node.split_range(start=range[0]-1, stop=range[1]))

    def _new_job_branch(self, reference: str) -> JobBranch:
        result = self._document_tree.create_job_branch(reference)
        self._append_to_gui(result)

        return result

    def _new_document_branch(
            self, job_branch: JobBranch, document_type: DocumentType
    ) -> DocumentBranch:
        result = job_branch.create_branch(document_type=document_type)
        self._append_to_gui(result)

        return result

    def _append_to_gui(self, node: AbstractNode) -> None:
        self._gui.AppendItem(
            parent=self._handle_from_node(node.parent),
            text=node.label,
            data=node.node_id
        )

    def _remove_from_gui(self, node: AbstractNode) -> None:
        self._gui.Delete(self._gui.get_item_handle(node_id=node.node_id))

    def _node_from_handle(self, handle: wx.TreeItemId) -> AbstractNode:
        return self._document_tree.child_by_id(
            node_id=self._gui.get_node_id(tree_handle=handle))

    def _handle_from_node(self, node: AbstractNode) -> wx.TreeItemId:
        return self._gui.get_item_handle(node.node_id)

    def _pending_leaves(self, file_paths: list[str]) -> list[PendingLeaf]:
        return [self._pending_leaf(file_path=path) for path in file_paths]

    def _pending_leaf(self, file_path: str) -> PendingLeaf:
        return PendingLeaf(
            parent=self._document_tree.pending_branch,
            file_name=ntpath.basename(file_path),
            data=rendering.render_images(file_path=file_path)
        )


class PageViewController:
    def __init__(self, gui: PageView):
        self._gui = gui
        self.canvas = gui.canvas

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self.canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self.canvas.Bind(wx.EVT_LEFT_DCLICK, self.fit_page_to_panel)

    def clear_display(self) -> None:
        self.canvas.ClearAll()
        self.canvas.ZoomToBB()

    def load_image(self, image: wx.Image) -> None:
        bitmap = FloatCanvas.ScaledBitmap(
            Bitmap=image, XY=(0,0), Height=image.GetHeight(), Position="bl")

        self.clear_display()
        self.canvas.AddObject(bitmap)
        self.canvas.ZoomToBB()

    def set_page_no(self, page_no) -> None:
        self._gui.page_no.SetValue(page_no)

    def set_total_pages(self, quantity: int or str) -> None:
        self._gui.set_total_pages(quantity)

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self.canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def fit_page_to_panel(self, _event: wx.EVT_LEFT_DCLICK = None):
        self.canvas.ZoomToBB()

    def bind_page_no(self, callback) -> None:
        self._gui.page_no.Bind(event=wx.EVT_SPINCTRL, handler=callback)

    def bind_delete(self, callback) -> None:
        self._gui.delete_button.Bind(event=wx.EVT_BUTTON, handler=callback)

    def bind_split_pages(self, callback) -> None:
        self._gui.split_button.Bind(event=wx.EVT_BUTTON, handler=callback)

    def show_all_widgets(self) -> None:
        self._gui.delete_button.Show()
        self._gui.split_button.Show()
        self._gui.page_no.Show()
        self._gui.page_quantity.Show()

    def hide_all_widgets(self) -> None:
        self._gui.delete_button.Hide()
        self._gui.split_button.Hide()
        self._gui.page_no.Hide()
        self._gui.page_quantity.Hide()

    def show_split_button(self) -> None:
        self._gui.split_button.Show()

    def hide_split_button(self) -> None:
        self._gui.split_button.Hide()


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
            self, root_application: RootInterface,
            config: AppConfiguration,
            window: Window
    ) -> None:
        self._root = root_application
        self._config = config

        self._gui = Viewer(window)
        window.set_panel(self._gui)

        file_menu = self._gui.file_menu

        window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_files,
            source=file_menu.import_files
        )

        window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_as,
            source=file_menu.import_prenamed_files
        )

        window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)

        self._gui.input_bar.submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._documents = DocumentController(self._gui)
        self._user_input = UserInputController(self._gui, self._config)
        self._window = window

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
        self._window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

