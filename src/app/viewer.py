import wx

from app.abstract_root import RootInterface
from app.configuration import AppConfiguration
from app.document import DocumentController
from app.user_input import UserInputController
from gui import Viewer


class ViewerApplicationController:
    def __init__(
            self, root_application: RootInterface, config: AppConfiguration
    ) -> None:
        
        self._root = root_application
        self._config = config

        self._gui = Viewer(self._root.window)
        self._root.window.set_panel(self._gui)

        file_menu = self._gui.file_menu

        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_files,
            source=file_menu.import_files
        )

        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_as,
            source=file_menu.import_prenamed_files
        )

        self._root.window.Bind(wx.EVT_MENU, self.on_quit, file_menu.quit)

        self._gui.input_bar.submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._documents = DocumentController(self._gui)
        self._user_input = UserInputController(self._gui, self._config)

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
        self._root.window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

