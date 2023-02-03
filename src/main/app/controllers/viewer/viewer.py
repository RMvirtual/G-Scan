import wx
from src.main.app.configuration import ViewerConfiguration
from src.main.app.controllers.viewer.page_canvas import PageCanvasController
from src.main.app.interfaces import RootInterface
from src.main.documents import rendering
from src.main.documents.processing import DocumentToProcess, DocumentWorkload
from src.main.gui import ImageViewer


class ViewerController:
    def __init__(
            self, root_application: RootInterface, config: ViewerConfiguration
    ) -> None:
        self._root = root_application
        self._config = config
        self._documents = DocumentWorkload()

        self._initialise_gui()
        self._bind_callbacks()

        self._page_controller = PageCanvasController(
            root_application=self._root, page_canvas=self._gui.page_canvas)

    def _initialise_gui(self) -> None:
        self._gui = ImageViewer(self._root.window)
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
        self._gui.bottom_toolbar.exit.Bind(wx.EVT_BUTTON, self.on_exit)
        self._gui.Bind(wx.EVT_CLOSE, self.on_close)
        self._bind_file_menu_callbacks()

    def _bind_file_menu_callbacks(self) -> None:
        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_files,
            source=self._gui.file_menu.import_files
        )

        self._root.window.Bind(
            event=wx.EVT_MENU, handler=self.on_import_files,
            source=self._gui.file_menu.import_files
        )

        self._root.window.Bind(
            wx.EVT_MENU, self.on_quit, self._gui.file_menu.quit)

    def on_import_files(self, event: wx.EVT_MENU) -> None:
        files = self._request_files_to_import()

        if not files:
            print("No files returned")

        else:
            for file in files:
                self._documents.pending.append(file)

            self._gui.file_tree.tree.AppendItem(
                parent=self._gui.file_tree.root_id,
                text=f"Pending ({len(self._documents.pending)})"
            )

            self.load(files[0])

    def _request_files_to_import(self) -> list[str]:
        browser_style = (wx.FD_MULTIPLE|wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        with wx.FileDialog(parent=self._gui, style=browser_style) as browser:
            if browser.ShowModal() == wx.ID_CANCEL:
                return []

            return browser.GetPaths()

    def on_import_prenamed_files(self, event: wx.EVT_MENU) -> None:
        print("Michelin Mode")

    def on_quit(self, event: wx.EVT_MENU = None) -> None:
        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_close(self, event = None) -> None:
        self._tear_down_gui()

    def _tear_down_gui(self) -> None:
        self._gui.Destroy()
        self._root.window.SetMenuBar(wx.MenuBar())

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

    def load(self, image_path: str) -> None:
        image = rendering.render(image_path)
        self._page_controller.load_image(image)