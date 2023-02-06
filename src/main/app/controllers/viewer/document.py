import wx
from src.main.documents.processing import PendingDocument, PendingDocuments
from src.main.gui.image_viewer.panels import FileTree
from src.main.gui import ImageViewer
from src.main.app.controllers.viewer.page_view import PageViewController


class DocumentController:
    def __init__(self, root_application, gui: ImageViewer):
        self._gui = gui

        self._page_view = PageViewController(
            root_application=root_application, page_canvas=self._gui.page_view)

        self.pending = PendingDocuments(self._gui.file_tree.tree)

    def on_tree_item(self, event = None) -> None:
        ...

    def import_files(self):
        files = self._request_files_to_import()

        if not files:
            return

        self._process_files(files)

    def add_pending_files(self, paths: list[str]) -> list[PendingDocument]:
        return [self.add_pending_file(path) for path in paths]

    def add_pending_file(self, path: str) -> PendingDocument:
        return self.pending.add_pending(file_path=path)

    def _bind_file_tree_callbacks(self) -> None:
        self._gui.tree.Bind(
            event=wx.EVT_TREE_SEL_CHANGED, handler=self.on_file_tree_selection)

    def on_file_tree_selection(self, event: wx.EVT_TREE_SEL_CHANGED) -> None:
        selections = self._gui.file_tree.tree.GetSelections()

        if len(selections) == 1:
            print("One Item Selected")

        elif len(selections) > 1:
            print("Multiple items selected.")

        else:
            print("No items selected apparently.")

    def _process_files(self, file_paths: list[str]) -> None:
        result = self.add_pending_files(paths=file_paths)
        self._page_view.load_image(result[0].images[0])

    def _request_files_to_import(self) -> list[str]:
        browser_style = (wx.FD_MULTIPLE|wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        with wx.FileDialog(parent=self._gui, style=browser_style) as browser:
            if browser.ShowModal() == wx.ID_CANCEL:
                return []

            return browser.GetPaths()
