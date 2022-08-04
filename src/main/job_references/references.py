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
    def FromFullReference(job_reference: str):
        digits = re.sub("\D", "", job_reference)  # Remove alphabet

        if len(digits) != 9:
            raise Exception("Incorrect number of digits.")

        # Get calendar date from reference number provided.
        date = calendar.date(
            int(digits[2:4]),
            int(digits[0:2])
        )

        gr_reference = GrReference(
            date=date,
            reference_number=digits[4:]
        )

        return gr_reference

    def add_quick_reference(self, job_reference: str):
        digits = re.sub("\D", "", job_reference)  # Remove alphabet

        if not (1 <= len(digits) <= 5):
            raise Exception("Incorrect number of digits.")

        self.pad_reference(digits)

    def pad_reference(self, brief_reference: str):
        # Needs edge case where date should be overwritten.
        self._job_reference = (
            "0" * (5-len(brief_reference)) + brief_reference)

    def as_string(self) -> str:
        return (
            "GR" +
            self._date.year_as_two_digits()
            + self._date.month_number_as_two_digits()
            + self._job_reference
        )
