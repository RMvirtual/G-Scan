import wx

from configuration import Configuration
from controllers.document_editor.document import DocumentController
from controllers.document_editor.user_input import UserInputController
from controllers.mediator import ApplicationMediator
from gui.document_editor import Viewer
from gui.window import Window


class DocumentEditorController:
    def __init__(
            self, root_application: ApplicationMediator,
            config: Configuration,
            window: Window
    ) -> None:
        self._root = root_application
        self._config = config
        self._window = window

        self._gui = Viewer(window)

        window.set_panel(self._gui)

        file_menu = self._gui.file_menu
        window.Bind(wx.EVT_MENU, self.on_import_files, file_menu.import_files)

        window.Bind(
            wx.EVT_MENU, self.on_import_as, file_menu.import_prenamed_files)

        window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)

        self._gui.input_bar.submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._documents = DocumentController(self._gui)
        self._user_input = UserInputController(self._gui, self._config)

    def on_submit(self, _event: wx.Event) -> None:
        submission_document = self._user_input.submission_document()

        if submission_document.reference:
            self._documents.submit(submission_document)

    def on_import_files(self, event: wx.Event) -> None:
        self._documents.import_files()

    def on_import_as(self, event: wx.Event) -> None:
        self._documents.import_as()

    def on_quit(self, event: wx.Event = None) -> None:
        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event = None) -> None:
        self._gui.Destroy()
        self._window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

