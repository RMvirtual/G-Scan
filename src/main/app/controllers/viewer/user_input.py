import wx
from src.main import documents
from src.main.app.configuration import ViewerConfiguration
from src.main.app.controllers.viewer.document import DocumentController
from src.main.app.interfaces import RootInterface
from src.main.documents import Document
from src.main.documents.references import JobReference
from src.main.gui import Viewer


class UserInputController:
    def __init__(self, gui: Viewer) -> None:
        self._gui = gui

    def job_reference(self) -> JobReference or None:
        reference = self._gui.input_bar.reference_input

        try:
            return JobReference(reference)

        except ValueError:
            message_box = wx.MessageDialog(
                parent=None, message=f"Job reference {reference} is invalid.",
                caption="Invalid Job Reference"
            )

            with message_box:
                message_box.ShowModal()

            return None

    def document_type(self) -> Document:
        return documents.load(full_name=self._gui.input_bar.document_type)