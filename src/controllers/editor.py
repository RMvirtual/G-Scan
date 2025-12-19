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
from rendering import MouseState, RenderingContext, Scene


class EditorController:
    def __init__(self, config: Configuration) -> None:
        self.config = config

        display_width, display_height = wx.DisplaySize()
        size = (int(display_width / 2), int(display_height / 1.1))

        self.gui = EditorFrame(size, position=wx.Point(size[0], 0))
        self.document_tree = DocumentTreeController(self.gui.tree_ctrl)
        self.current_document: DocumentEntry = None

        # Rendering context.
        self.rendering_context = RenderingContext(self.gui.canvas)
        self.mouse = MouseState()
        self.scene = Scene()

        # Update GUI.
        departments = [d.full_name for d in self.config.departments]
        self.gui.job_entry_toolbar.department_box.Set(departments)
        self.gui.job_entry_toolbar.department_box.SetValue(departments[0])

        document_types = [
            d.full_name for d in self.config.department.document_types
        ]

        self.gui.job_entry_toolbar.document_box.Set(document_types)
        self.gui.job_entry_toolbar.document_box.SetValue(document_types[0])
        self.gui.job_entry_toolbar.Fit()

        # Canvas event handlers.
        self.gui.canvas.Bind(wx.EVT_PAINT, self.on_paint)
        self.gui.canvas.Bind(wx.EVT_LEFT_DOWN, self.on_canvas_left_down)
        self.gui.canvas.Bind(wx.EVT_MOTION, self.on_canvas_motion)
        self.gui.canvas.Bind(wx.EVT_LEAVE_WINDOW, self.on_canvas_leave)
        self.gui.canvas.Bind(wx.EVT_LEFT_UP, self.on_canvas_left_up)
        self.gui.canvas.Bind(wx.EVT_SIZE, self.on_canvas_resize)
        self.gui.canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_canvas_mouse_wheel)

        self.gui.canvas_toolbar.camera_zoom_combobox.Bind(
            wx.EVT_COMBOBOX, self.on_zoom_level_selection
        )

        # Job entry toolbar event handlers.
        entry_toolbar = self.gui.job_entry_toolbar
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

        self.scene.camera.dimensions = Vector2D.fromPoint(self.gui.canvas.Size)
        self.render()

    def render(self) -> None:
        self.rendering_context.render(self.scene, self.mouse)

    def on_paint(self, event: wx.Event) -> None:
        self.rendering_context.swap_buffers()

    def on_canvas_left_down(self, event: wx.MouseEvent) -> None:
        self.mouse.click_down(event)

        self.render()
        self.gui.canvas.Refresh(False)

    def on_canvas_left_up(self, event: wx.MouseEvent) -> None:
        self.mouse.click_release(event)

        self.render()
        self.gui.canvas.Refresh(False)

    def on_canvas_motion(self, event: wx.MouseEvent) -> None:
        self.mouse.motion(event)
        self.scene.camera.position -= self.mouse.drag_distance()

        toolbar = self.gui.canvas_toolbar
        toolbar.camera_x_entry.SetValue(f"{self.scene.camera.position.x:.1f}")
        toolbar.camera_y_entry.SetValue(f"{self.scene.camera.position.y:.1f}")

        self.render()
        self.gui.canvas.Refresh(False)

    def on_canvas_leave(self, event: wx.MouseEvent) -> None:
        self.mouse.click_release(event)
        self.gui.canvas.Refresh(False)

    def on_canvas_mouse_wheel(self, event: wx.MouseEvent) -> None:
        self.scene.camera.zoom += event.WheelRotation // 120 * 0.1

        self.render()
        self.gui.canvas.Refresh(False)

    def on_canvas_resize(self, event: wx.SizeEvent) -> None:
        self.scene.camera.dimensions = Vector2D.fromPoint(event.Size)

        self.render()
        self.gui.canvas.Refresh(False)

    def on_zoom_level_selection(self, event: wx.CommandEvent) -> None:
        zoom = float(event.String.removesuffix("%"))
        self.scene.camera.zoom = zoom / 100

    def change_department(self, department: Department) -> None:
        if self.config.department == department:
            return

        self.config.department = department

        available_document_types = [
            d.full_name for d in self.config.department.document_types
        ]

        document_type_box = self.gui.job_entry_toolbar.document_box
        document_type_box.Set(available_document_types)

        if document_type_box.GetValue() not in available_document_types:
            new_type = self.config.department.document_types[0]
            self.config.document_type = new_type
            document_type_box.SetValue(new_type.full_name)

    def on_submit(self, event: wx.Event) -> None:
        try:
            toolbar = self.gui.job_entry_toolbar
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
        document_bitmap = entry.pages[0]

        bitmap_copy = document_bitmap.GetSubBitmap(
            wx.Rect(0, 0, document_bitmap.Width, document_bitmap.Height)
        )

        self.scene = Scene(bitmap_copy)
        self.scene.camera.dimensions = Vector2D.fromPoint(self.gui.canvas.Size)

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
        box = self.gui.job_entry_toolbar.department_box
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
