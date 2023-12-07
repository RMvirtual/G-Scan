import wx
from src.main import documents
from src.main.app.configuration import ViewerConfiguration
from src.main.documents import Document
from src.main.documents.references import AbstractReference, JobReference
from src.main.gui import Viewer


class SubmissionDocument:
    def __init__(self, reference: AbstractReference, document_type: Document):
        self.reference = reference
        self.document_type = document_type


class UserInputController:
    def __init__(self, gui: Viewer, config: ViewerConfiguration) -> None:
        self._gui = gui
        self._config = config
        self._input_bar = self._gui.input_bar

        self._load_department()
        self._load_document()

    def _load_department(self):
        names = self._config.all_departments.full_names()
        self._input_bar.department_options = names

        current_department = self._config.department.full_name
        self._input_bar.department = current_department

    def _load_document(self) -> None:
        names = self._config.department.document_types.full_names()
        self._input_bar.document_options = names

        current_document = self._config.document_type.full_name
        self._input_bar.document_type = current_document

    def submission_document(self) -> SubmissionDocument:
        return SubmissionDocument(
            reference=self.job_reference(),
            document_type=self.document_type()
        )

    def job_reference(self) -> JobReference or None:
        reference = self._input_bar.reference_input

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
        return documents.load(full_name=self._input_bar.document_type)