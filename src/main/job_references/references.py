import re
from src.main.date.date import Date
import src.main.date.calendar as calendar


class GrReference:
    def __init__(self, date: Date = None, job_number: str = None):
        self._prefix = "GR"
        self._date = date
        self._job_number = job_number

    @staticmethod
    def TemplateReference(date: Date):
        return GrReference(date=date, job_number="00000")

    @staticmethod
    def FullReference(job_reference: str):
        digits = GrReference._extract_digits_from_string(job_reference)

        if not GrReference._digits_are_valid_full_reference(digits):
            raise ValueError("Incorrect number of digits.")

        date = GrReference._date_from_full_reference(digits)

        return GrReference(date=date, job_number=digits[4:])

    def set_job_number(self, job_number: str):
        digits = self._extract_digits_from_string(job_number)

        if not self._digits_are_valid_job_number(digits):
            raise ValueError("Incorrect number of digits.")

        self._pad_reference(digits)

    def _pad_reference(self, brief_reference: str):
        # Needs edge case where date should be overwritten.
        self._job_number = (
            "0" * (5-len(brief_reference)) + brief_reference)

    @staticmethod
    def _date_from_full_reference(digits: str) -> Date:
        year_digits = int(digits[0:2])
        month_digits = int(digits[2:4])

        return calendar.date(month=month_digits, year=year_digits)

    @staticmethod
    def _digits_are_valid_full_reference(digits: str):
        return len(digits) == 9 and digits.isnumeric()

    @staticmethod
    def _digits_are_valid_job_number(digits: str):
        return 1 <= len(digits) <= 5 and digits.isnumeric()

    @staticmethod
    def _extract_digits_from_string(string: str):
        return re.sub("\\D", "", string)

    def _date_prefix(self) -> str:
        return (
            self._date.year_as_two_digits() +
            self._date.month_number_as_two_digits()
        )

    def to_string(self) -> str:
        return self._prefix + self._date_prefix() + self._job_number
