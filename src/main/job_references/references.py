import re
from src.main.date.date import Date
import src.main.date.calendar as calendar


class GrReference:
    def __init__(self, date: Date = None, reference_number: str = None):
        self._date = date
        self._job_reference = reference_number

    @staticmethod
    def TemplateReference(date: Date):
        return GrReference(date=date, reference_number="00000")

    @staticmethod
    def FromFullReference(reference_number: str):
        # Get calendar date from reference number provided.
        date = calendar.date(reference_number[2:4], reference_number[0:2])

        gr_reference = GrReference(
            date=date,
            reference_number=reference_number[5:]
        )

        return gr_reference

    def _is_full_input_length(self, inputted_reference: str) -> bool:
        return len(inputted_reference) == 9

    def _is_quick_input_length(self, inputted_reference: str) -> bool:
        return 4 <= len(inputted_reference) <= 9

    def _strip_alphabet(self, string_to_modify: str) -> str:
        return re.sub("[^0-9]", "", string_to_modify)

    def pad_reference(self, brief_reference: str):
        self._job_reference = brief_reference

    def as_string(self) -> str:
        return "GR" + self._strip_alphabet(
            self._date.year_as_two_digits()
            + self._date.month_number_as_two_digits()
            + self._job_reference
        )
