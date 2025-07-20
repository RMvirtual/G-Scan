import wx
from wx.lib.floatcanvas import FloatCanvas

from controllers.editor.document_tree import DocumentTreeController
from data_structures_new import Branch, DocumentEntry
from document_tree import DocumentType
from gui.editor import EditorPanel


class DocumentController:
    def __init__(self, gui: EditorPanel) -> None:
        self.gui = gui

        self.document_tree = DocumentTreeController(self.gui.tree_ctrl)

        # Event handlers.
        page_view = self.gui.page_canvas
        page_view.Canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_canvas_wheel)
        page_view.Canvas.Bind(wx.EVT_LEFT_DCLICK, self.on_canvas_click)
        page_view.page_no_spin_ctrl.Bind(wx.EVT_SPINCTRL, self.on_page_no_btn)
        page_view.delete_btn.Bind(wx.EVT_BUTTON, self.on_delete_btn)
        page_view.split_btn.Bind(wx.EVT_BUTTON, self.on_split_pages_btn)

        self.gui.tree_ctrl.Bind(
            wx.EVT_TREE_SEL_CHANGED, self.on_item_selection
        )

        self.hide_document_entry_tools()
        self.current_document: DocumentEntry = None

    def import_files(self):
        dialog = wx.FileDialog(
            parent=None,
            style=(wx.FD_MULTIPLE | wx.FD_OPEN | wx.FD_FILE_MUST_EXIST),
        )

        with dialog:
            dialog.ShowModal()

        files = dialog.GetPaths()

        if files:
            pending_items = self.document_tree.create_pending_files(files)
            self.view_document_entry(pending_items[0])

    def import_as(self) -> None:
        print("Michelin Mode")

    def view_document_entry(self, entry: DocumentEntry) -> None:
        # Set page total.
        no_of_pages = len(entry.pages)
        page_view = self.gui.page_canvas
        page_view.page_qty_text.SetValue(f"Total Pages: {no_of_pages}")
        page_view.page_no_spin_ctrl.SetMin(1)
        page_view.page_no_spin_ctrl.SetMax(no_of_pages)
        self.show_document_entry_tools()

        self.current_document = entry
        self.view_page(0)

    def view_page(self, page_no: int) -> None:
        image: wx.Image = self.current_document.pages[page_no]

        bitmap = FloatCanvas.ScaledBitmap(
            Bitmap=image, XY=(0, 0), Height=image.GetHeight(), Position="bl"
        )

        self.clear_canvas()
        self.gui.page_canvas.Canvas.AddObject(bitmap)
        self.gui.page_canvas.Canvas.ZoomToBB()
        self.gui.page_canvas.page_no_spin_ctrl.SetValue(page_no + 1)

    def clear_view(self) -> None:
        self.current_document = None
        self.clear_canvas()

    def clear_canvas(self) -> None:
        self.gui.page_canvas.Canvas.ClearAll()
        self.gui.page_canvas.Canvas.ZoomToBB()

    def assign_current_document(
        self, reference: str, document_type: DocumentType
    ) -> None:
        self.document_tree.move_entry(
            self.current_document, reference, document_type
        )

        self.document_tree.create_job_node(
            reference, document_type, leaf=self.current_document
        )

    def show_document_entry_tools(self) -> None:
        view = self.gui.page_canvas
        view.delete_btn.Show()
        view.split_btn.Show()
        view.page_no_spin_ctrl.Show()
        view.page_qty_text.Show()

    def hide_document_entry_tools(self) -> None:
        view = self.gui.page_canvas

        view.delete_btn.Hide()
        view.split_btn.Hide()
        view.page_no_spin_ctrl.Hide()
        view.page_qty_text.Hide()

    def on_canvas_wheel(self, event: wx.MouseEvent) -> None:
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self.gui.page_canvas.Canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True
        )

    def on_canvas_click(self, event: wx.Event) -> None:
        self.gui.page_canvas.Canvas.ZoomToBB()

    def on_split_pages_btn(self, event: wx.Event) -> None:
        self.document_tree.split_pages(self.current_document)

    def on_page_no_btn(self, event: wx.Event) -> None:
        self.view_page(page_no=event.Position - 1)

    def on_delete_btn(self, event: wx.Event) -> None:
        self.document_tree.delete_current()
        self.clear_canvas()

    def on_item_selection(self, event: wx.TreeEvent) -> None:
        entry = self.document_tree.gui.GetItemData(event.Item)

        if isinstance(entry, Branch):
            self.document_tree.gui.Expand(entry.gui_id)
            self.hide_document_entry_tools()
            self.clear_view()
            self.gui.page_canvas.split_btn.Hide()

        elif isinstance(entry, DocumentEntry):
            self.view_document_entry(entry)

        else:
            self.hide_document_entry_tools()
            self.clear_view()
