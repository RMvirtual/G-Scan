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
        self._root = root_application
        self._config = config
        self._window = window

        self._gui = Viewer(window)

        window.set_panel(self._gui)

        file_menu = self._gui.file_menu
        window.Bind(wx.EVT_MENU, self.on_import_files, file_menu.import_files)

        window.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files
        )

        window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)

        self._gui.input_bar.submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._documents = DocumentController(self._gui)

    def on_submit(self, _event: wx.Event) -> None:
        try:
            input_bar = self._gui.input_bar
            reference = create_job_reference(input_bar.reference_input)

            document_type = self._config.database.document(
                full_name=input_bar.document_type
            )

            self._documents.assign_current_document(reference, document_type)

        except ValueError as error:
            message_box = wx.MessageDialog(
                parent=None,
                message=str(error),
                caption="Submission Failure",
            )

            with message_box:
                message_box.ShowModal()

    def on_import_files(self, event: wx.Event) -> None:
        self._documents.import_files()

    def on_import_as(self, event: wx.Event) -> None:
        self._documents.import_as()

    def on_quit(self, event: wx.Event = None) -> None:
        self._exit_to_main_menu()

    def on_exit(self, event=None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event=None) -> None:
        self._gui.Destroy()
        self._window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()
