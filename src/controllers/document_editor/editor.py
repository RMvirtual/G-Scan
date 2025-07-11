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
        file_menu = self.gui.file_menu

        self.window.Bind(
            wx.EVT_MENU, self.on_import_files, file_menu.import_files
        )

        self.window.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files
        )

        self.window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)
        self.gui.input_bar.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        self.gui.Bind(wx.EVT_CLOSE, self.on_close)
        self.gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

    def on_submit(self, event: wx.Event) -> None:
        try:
            reference = create_job_reference(
                self.gui.input_bar.reference_input.GetValue()
            )

            document_type = self.config.database.document(
                full_name=self.gui.input_bar.document_combobox.GetValue()
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

    def on_quit(self, event: wx.Event = None) -> None:
        self._exit_to_main_menu()

    def on_exit(self, event=None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event=None) -> None:
        self.gui.Destroy()
        self.window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self.gui.Close()
        self.root.launch_main_menu()
