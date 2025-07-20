import wx

from configuration import Configuration
from controllers.editor.document import DocumentController
from controllers.mediator import ApplicationMediator
from controllers.settings import SettingsDialogController
from gui.editor import EditorPanel
from gui.settings_dialog import SettingsDialog
from gui.window import Window
from job_references import create_job_reference


class EditorController:
    def __init__(
        self,
        root_application: ApplicationMediator,
        config: Configuration,
        window: Window,
    ) -> None:
        self.root = root_application
        self.config = config
        self.window = window
        self.gui = EditorPanel(window)
        self.window.set_panel(self.gui)
        self.documents = DocumentController(self.gui)

        # Event handlers.
        self.gui.entry_toolbar.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        self.gui.exit_btn.Bind(wx.EVT_BUTTON, self.on_f4_escape_key)

        # Top menu bar handlers.
        file_menu = self.gui.menu_bar.file

        self.window.Bind(
            wx.EVT_MENU, self.on_import_files, file_menu.import_files
        )

        self.window.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files
        )

        self.window.Bind(wx.EVT_MENU, self.on_exit, file_menu.quit)

        settings_menu = self.gui.menu_bar.settings
        self.window.Bind(wx.EVT_MENU, self.on_settings, settings_menu.settings)

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

    def on_settings(self, event: wx.Event) -> None:
        controller = SettingsDialogController(self.root, self.gui, self.config)
        controller.poll()

    def on_exit(self, event=None) -> None:
        self.gui.Destroy()
        self.window.SetMenuBar(wx.MenuBar())
        self.root.exit()

    def on_f4_escape_key(self, event: wx.Event) -> None:
        self.on_exit(event)
