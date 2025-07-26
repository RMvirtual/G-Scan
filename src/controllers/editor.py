import calendar
import datetime

import wx
from wx.lib.floatcanvas import FloatCanvas

from configuration import Configuration
from controllers.document_tree_ import DocumentTreeController
from controllers.settings import SettingsDialogController
from data_structures_new import Branch, DocumentEntry
from departments import Department
from document_tree import DocumentType
from gui.editor import EditorPanel
from job_references import create_job_reference


class EditorController:
    def __init__(self, config: Configuration) -> None:
        self.config = config

        display_width, display_height = wx.DisplaySize()
        size = (int(display_width / 2), int(display_height / 1.1))

        self.gui = EditorPanel(size, position=wx.Point(size[0], 0))
        self.document_tree = DocumentTreeController(self.gui.tree_ctrl)
        self.current_document: DocumentEntry = None

        self.hide_document_entry_tools()

        # Update GUI.
        departments = [d.full_name for d in self.config.departments]
        self.gui.entry_toolbar.department_box.Set(departments)
        self.gui.entry_toolbar.department_box.SetValue(departments[0])

        document_types = [
            d.full_name for d in self.config.department.document_types
        ]

        self.gui.entry_toolbar.document_box.Set(document_types)
        self.gui.entry_toolbar.document_box.SetValue(document_types[0])
        self.gui.entry_toolbar.Fit()

        # Event handlers.
        page_view = self.gui.page_canvas
        page_view.Canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_canvas_wheel)
        page_view.Canvas.Bind(wx.EVT_LEFT_DCLICK, self.on_canvas_click)
        page_view.delete_btn.Bind(wx.EVT_BUTTON, self.on_delete_btn)
        page_view.split_btn.Bind(wx.EVT_BUTTON, self.on_split_pages_btn)

        entry_toolbar = self.gui.entry_toolbar
        entry_toolbar.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)

        entry_toolbar.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_change
        )

        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_f4_escape_key)

        self.gui.tree_ctrl.Bind(
            wx.EVT_TREE_SEL_CHANGED, self.on_item_selection
        )

        self.gui.page_canvas.page_no_spin_ctrl.Bind(
            wx.EVT_SPINCTRL, self.on_page_no_btn
        )

        # Top menu bar handlers.
        file_menu = self.gui.menu_bar.file

        self.gui.Bind(
            wx.EVT_MENU, self.on_import_files, file_menu.import_files
        )

        self.gui.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files
        )

        self.gui.Bind(wx.EVT_MENU, self.on_exit, file_menu.quit)

        settings_menu = self.gui.menu_bar.settings
        self.gui.Bind(wx.EVT_MENU, self.on_settings, settings_menu.settings)

        # Shortcut keys.
        f4_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4_escape_key, id=f4_shortcut_id)

        esc_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4_escape_key, id=esc_shortcut_id)

        accelators = [
            (wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id),
            (wx.ACCEL_NORMAL, wx.WXK_ESCAPE, esc_shortcut_id),
        ]

        self.gui.SetAcceleratorTable(wx.AcceleratorTable(accelators))

        self.gui.SetFocus()
        self.gui.Show()

    def change_department(self, department: Department) -> None:
        if self.config.department == department:
            return

        self.config.department = department

        available_document_types = [
            d.full_name for d in self.config.department.document_types
        ]

        document_type_box = self.gui.entry_toolbar.document_box
        document_type_box.Set(available_document_types)

        if document_type_box.GetValue() not in available_document_types:
            new_type = self.config.department.document_types[0]
            self.config.document_type = new_type
            document_type_box.SetValue(new_type.full_name)

    def on_submit(self, event: wx.Event) -> None:
        try:
            toolbar = self.gui.entry_toolbar
            inputted_numbers = toolbar.reference_input.GetValue()

            if len(inputted_numbers) < 9:
                month = toolbar.month_box.GetValue()
                year = toolbar.year_box.GetValue()
                date = datetime.datetime(year, month)
                reference = create_job_reference(inputted_numbers, date)

            else:
                reference = create_job_reference(inputted_numbers)

            document_type = self.config.database.document(
                full_name=toolbar.document_box.GetValue()
            )

            self.assign_current_document(reference, document_type)

        except ValueError as error:
            message_box = wx.MessageDialog(
                parent=None,
                message=str(error),
                caption="Submission Failure",
            )

            with message_box:
                message_box.ShowModal()

    def on_import_files(self, event: wx.Event) -> None:
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

    def on_page_no_btn(self, event: wx.Event) -> None:
        self.view_page(page_no=event.Position - 1)

    def on_import_as(self, event: wx.Event) -> None:
        print("Michelin Mode")

    def on_settings(self, event: wx.Event) -> None:
        controller = SettingsDialogController(self.gui, self.config)
        controller.poll()

    def on_exit(self, event: wx.Event) -> None:
        self.gui.Destroy()

    def on_department_change(self, event: wx.Event) -> None:
        box = self.gui.entry_toolbar.department_box
        selection = box.GetValue()

        matching_departments = list(
            filter(lambda d: d.full_name == selection, self.config.departments)
        )

        if not matching_departments:
            raise ValueError(
                f"Could not find available departments matching {selection}"
            )

        self.change_department(matching_departments[0])

    def on_f4_escape_key(self, event: wx.Event) -> None:
        self.on_exit(event)

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

    def on_delete_btn(self, event: wx.Event) -> None:
        self.document_tree.delete_current()
        self.clear_canvas()
