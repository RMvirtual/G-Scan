import wx
from src.main import documents
from src.main.app.configuration import ViewerConfiguration
from src.main.app.controllers.viewer.document import DocumentController
from src.main.app.interfaces import RootInterface
from src.main.documents.references import JobReference
from src.main.gui import Viewer
from src.main.app.controllers.viewer.user_input import UserInputController


class ViewerApplicationController:
    def __init__(
            self, root_application: RootInterface, config: ViewerConfiguration
    ) -> None:
        self._root = root_application
        self._config = config

        self._initialise_gui()
        self._bind_callbacks()

        self._documents = DocumentController(gui=self._gui)
        self._user_input = UserInputController(gui=self._gui)

    def _initialise_gui(self) -> None:
        self._gui = Viewer(self._root.window)
        self._root.window.set_panel(self._gui)
        self._initialise_department_box()
        self._initialise_document_box()

    def _initialise_department_box(self):
        department_names = self._config.all_departments.full_names()
        self._gui.input_bar.department_options = department_names

        current_department = self._config.department.full_name
        self._gui.input_bar.department = current_department

    def _initialise_document_box(self) -> None:
        document_names = self._config.department.document_types.full_names()
        self._gui.input_bar.document_options = document_names

        current_document = self._config.document_type.full_name
        self._gui.input_bar.document_type = current_document

    def _bind_callbacks(self) -> None:
        self._bind_file_menu_callbacks()
        self._bind_user_input_callbacks()
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._gui.bottom_bar.exit.Bind(wx.EVT_BUTTON, self.on_exit)

    def _bind_user_input_callbacks(self) -> None:
        self._gui.input_bar.submit.Bind(
            event=wx.EVT_BUTTON, handler=self.on_submit)

    def _bind_file_menu_callbacks(self) -> None:
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

    def on_submit(self, _event: wx.EVT_BUTTON) -> None:
        document_type = self._user_input.document_type()
        job_reference = self._user_input.job_reference()

        if job_reference:
            self._documents.submit(
                reference=job_reference, document_type=document_type)

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

