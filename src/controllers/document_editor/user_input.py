import dataclasses

import wx

from configuration import Configuration
from documents import DocumentType
from gui.document_editor import Viewer
from job_references import create_job_reference


@dataclasses.dataclass
class SubmissionDocument:
    reference: str
    document_type: DocumentType


class UserInputController:
    def __init__(self, gui: Viewer, config: Configuration) -> None:
        self._gui = gui
        self._config = config

        self._input_bar = self._gui.input_bar

        departments = list(
            map(lambda dept: dept.full_name, self._config.departments)
        )

        self._input_bar.department_options = departments

        current_department = self._config.department.full_name
        self._input_bar.department = current_department

        documents = list(
            map(lambda d: d.full_name, self._config.department.document_types)
        )

        self._input_bar.document_options = documents

        current_document = self._config.document_type.full_name
        self._input_bar.document_type = current_document

    def submission_document(self) -> SubmissionDocument | None:
        try:
            reference = create_job_reference(self._input_bar.reference_input)

            document_type = self._config.database.document(
                full_name=self._input_bar.document_type
            )

            return SubmissionDocument(reference, document_type)

        except ValueError as error:
            message_box = wx.MessageDialog(
                parent=None,
                message=str(error),
                caption="Submission Failure",
            )

            with message_box:
                message_box.ShowModal()

            return None
