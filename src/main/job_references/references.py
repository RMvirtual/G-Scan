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
    def FullReference(job_reference: str):
        digits = GrReference._extract_digits(job_reference)

        if not GrReference._is_full_length(digits):
            raise ValueError("Incorrect number of digits.")
            # More specific error required.

        date = calendar.date(
            int(digits[2:4]),
            int(digits[0:2])
        )

        return GrReference(
            date=date,
            reference_number=digits[4:]
        )

    def add_quick_reference(self, job_reference: str):
        digits = self._extract_digits(job_reference)

        if not self._is_quick_reference_length(digits):
            raise ValueError("Incorrect number of digits.")

        self._pad_reference(digits)

    def _pad_reference(self, brief_reference: str):
        # Needs edge case where date should be overwritten.
        self._job_reference = (
            "0" * (5-len(brief_reference)) + brief_reference)

    @staticmethod
    def _is_full_length(digits: str):
        return len(digits) == 9

    @staticmethod
    def _is_quick_reference_length(digits: str):
        return 1 <= len(digits) <= 5

    @staticmethod
    def _extract_digits(string: str):
        """Strip all characters from a string except digits."""

        return re.sub("\\D", "", string)

    def as_string(self) -> str:
        return (
            "GR" +
            self._date.year_as_two_digits()
            + self._date.month_number_as_two_digits()
            + self._job_reference
        )
