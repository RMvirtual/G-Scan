import wx

from configuration import Configuration
from controllers.document_editor.document import DocumentController
from controllers.mediator import ApplicationMediator
from gui.document_editor import Viewer
from gui.window import Window
from job_references import create_job_reference


class DocumentEditorController:
    def __init__(
        self,
        root_application: ApplicationMediator,
        config: Configuration,
        window: Window,
    ) -> None:
        self.root = root_application
        self.config = config
        self.window = window
        self.gui = Viewer(window)
        self.window.set_panel(self.gui)
        self.documents = DocumentController(self.gui)

        # Event handlers.
        self.gui.entry_toolbar.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_f4)

        # File menu handlers.
        file_menu = self.gui.file_menu

        self.window.Bind(
            wx.EVT_MENU, self.on_import_files, file_menu.import_files
        )

        self.window.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files
        )

        self.window.Bind(wx.EVT_MENU, self.on_exit, file_menu.quit)

        # Shortcut keys.
        f4_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4, id=f4_shortcut_id)

        escape_shortcut_id = wx.NewId()
        self.gui.Bind(wx.EVT_MENU, self.on_f4, id=escape_shortcut_id)

        accelators = [
            (wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id),
            (wx.ACCEL_NORMAL, wx.WXK_ESCAPE, escape_shortcut_id),
        ]

        self.gui.SetAcceleratorTable(wx.AcceleratorTable(accelators))
        self.gui.SetFocus()

    def on_submit(self, event: wx.Event) -> None:
        try:
            reference = create_job_reference(
                self.gui.entry_toolbar.reference_text.GetValue()
            )

            document_type = self.config.database.document(
                full_name=self.gui.entry_toolbar.document_box.GetValue()
            )

            self.documents.assign_current_document(reference, document_type)

        except ValueError as error:
            message_box = wx.MessageDialog(
                parent=None,
                message=str(error),
                caption="Submission Failure",
            )

            with message_box:
                message_box.ShowModal()

    def on_import_files(self, event: wx.Event) -> None:
        self.documents.import_files()

    def on_import_as(self, event: wx.Event) -> None:
        self.documents.import_as()

    def on_f4(self, event: wx.Event) -> None:
        self.on_exit(event)

    def on_exit(self, event=None) -> None:
        self.gui.Destroy()
        self.window.SetMenuBar(wx.MenuBar())
        self.root.launch_main_menu()
