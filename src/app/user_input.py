import wx

from app.configuration import AppConfiguration
from documents import Document
from job_references import GrReference
from gui import Viewer


class SubmissionDocument:
    def __init__(self, reference: GrReference, document_type: Document):
        self.reference = reference
        self.document_type = document_type


class UserInputController:
    def __init__(self, gui: Viewer, config: AppConfiguration) -> None:
        self._gui = gui
        self._config = config

        self._input_bar = self._gui.input_bar
        self._load_department()
        self._load_document()

    def _load_department(self):
        names = list(map(
            lambda dept: dept.full_name, self._config.departments))
        
        self._input_bar.department_options = names

        current_department = self._config.department.full_name
        self._input_bar.department = current_department

    def _load_document(self) -> None:
        names = list(map(
            lambda d: d.full_name, self._config.department.document_types))

        self._input_bar.document_options = names

        current_document = self._config.document_type.full_name
        self._input_bar.document_type = current_document

    def submission_document(self) -> SubmissionDocument:
        return SubmissionDocument(self.job_reference(), self.document_type())

    def job_reference(self) -> GrReference or None:
        reference = self._input_bar.reference_input

        try:
            return GrReference(reference)

        except ValueError:
            message_box = wx.MessageDialog(
                parent=None, message=f"Job reference {reference} is invalid.",
                caption="Invalid Job Reference"
            )

            with message_box:
                message_box.ShowModal()

            return None

    def document_type(self) -> Document:
        return self._config.database.document(
            full_name=self._input_bar.document_type)
    