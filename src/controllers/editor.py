import datetime

import wx

from configuration import Configuration
from controllers.document_tree_ import DocumentTreeController
from controllers.settings import SettingsDialogController
from data_structures_new import Branch, DocumentEntry
from departments import Department
from document_tree import DocumentType
from gui.editor import EditorFrame
from job_references import create_job_reference
from maths import Vector2D


class EditorController:
    def __init__(self, config: Configuration) -> None:
        self.config = config

        display_width, display_height = wx.DisplaySize()
        size = (int(display_width / 2), int(display_height / 1.1))

        self.gui = EditorFrame(size, position=wx.Point(size[0], 0))
        self.document_tree = DocumentTreeController(self.gui.tree_ctrl)
        self.current_document: DocumentEntry = None

        # Rendering context.
        self.buffer: wx.Bitmap = None
        self.page_bitmap: wx.Bitmap = None
        self.document_bitmap: wx.Bitmap = None
        self.camera_xy = Vector2D(0, 0)
        self.mouse_position: Vector2D = None
        self.last_drag: Vector2D = None
        self.mouse_down = False

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
        self.gui.page_canvas.Bind(wx.EVT_PAINT, self.on_paint)
        self.gui.page_canvas.Bind(wx.EVT_LEFT_DOWN, self.on_canvas_left_down)
        self.gui.page_canvas.Bind(wx.EVT_MOTION, self.on_canvas_drag)
        self.gui.page_canvas.Bind(wx.EVT_LEAVE_WINDOW, self.on_canvas_leave)
        self.gui.page_canvas.Bind(wx.EVT_LEFT_UP, self.on_canvas_left_up)
        self.gui.page_canvas.Bind(wx.EVT_SIZE, self.on_canvas_resize)

        entry_toolbar = self.gui.entry_toolbar
        entry_toolbar.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)

        entry_toolbar.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_change
        )

        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_f4_escape_key)

        self.gui.tree_ctrl.Bind(
            wx.EVT_TREE_SEL_CHANGED, self.on_item_selection
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
        self.render()

    def render(self) -> None:
        bitmap_size = self.gui.page_canvas.Size
        self.buffer = wx.Bitmap(bitmap_size)
        device_context = wx.MemoryDC(self.buffer)

        device_context.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        device_context.Clear()

        if self.current_document:
            bitmap = self.document_bitmap.GetSubBitmap(
                wx.Rect(self.camera_xy.x, self.camera_xy.y, 400, 400)
            )

            wx.Bitmap.Rescale(bitmap, bitmap_size)
            device_context.DrawBitmap(bitmap, 0, 0, False)

        if self.mouse_down:
            # Black box signifying mouse motion.
            device_context.SetPen(wx.Pen(wx.Colour(0, 0, 0)))

            device_context.DrawRectangle(
                self.mouse_position.x - 25,
                self.mouse_position.y - 25,
                50,
                50,
            )

        device_context.SelectObject(wx.NullBitmap)

    def on_paint(self, event: wx.Event) -> None:
        self.page_bitmap = self.buffer
        device_context = wx.PaintDC(self.gui.page_canvas)
        device_context.DrawBitmap(self.page_bitmap, 0, 0, useMask=False)

    def on_canvas_left_down(self, event: wx.MouseEvent) -> None:
        self.mouse_position = Vector2D.fromPoint(event.Position)
        self.last_drag = Vector2D.fromPoint(event.Position)
        self.mouse_down = True
        self.render()

        self.gui.page_canvas.Refresh(False)

    def on_canvas_drag(self, event: wx.MouseEvent) -> None:
        if not self.mouse_down:
            return

        self.last_drag = self.mouse_position
        self.mouse_position = Vector2D.fromPoint(event.Position)
        drag_distance = self.mouse_position - self.last_drag
        self.camera_xy = self.camera_xy - drag_distance

        if self.camera_xy.x < 0:
            self.camera_xy.x = 0

        if self.camera_xy.y < 0:
            self.camera_xy.y = 0

        if self.document_bitmap is not None:
            if self.camera_xy.x > self.document_bitmap.Width:
                self.camera_xy.x = self.document_bitmap.Width

            if self.camera_xy.y > self.document_bitmap.Height:
                self.camera_xy.y = self.document_bitmap.Height

        self.render()
        self.gui.page_canvas.Refresh(False)

    def on_canvas_leave(self, event: wx.MouseEvent) -> None:
        self.mouse_down = False

        # self.render()
        self.gui.page_canvas.Refresh(False)

    def on_canvas_left_up(self, event: wx.MouseEvent) -> None:
        self.mouse_position = None
        self.last_drag = None
        self.mouse_down = False

        self.render()
        self.gui.page_canvas.Refresh(False)

    def on_canvas_resize(self, event: wx.MouseEvent) -> None:
        self.render()
        self.gui.page_canvas.Refresh(False)

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
        self.current_document = entry
        original_bitmap = entry.pages[0]

        bitmap = original_bitmap.GetSubBitmap(
            wx.Rect(0, 0, original_bitmap.Width, original_bitmap.Height)
        )

        self.document_bitmap = bitmap

    def on_item_selection(self, event: wx.TreeEvent) -> None:
        entry = self.document_tree.gui.GetItemData(event.Item)

        if isinstance(entry, Branch):
            self.document_tree.gui.Expand(entry.gui_id)
            self.clear_view()

        elif isinstance(entry, DocumentEntry):
            self.view_document_entry(entry)

        else:
            self.clear_view()

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

    def assign_current_document(
        self, reference: str, document_type: DocumentType
    ) -> None:
        self.document_tree.move_entry(
            self.current_document, reference, document_type
        )

        self.document_tree.create_job_node(
            reference, document_type, leaf=self.current_document
        )
