import re
from src.main.date.date import Date
import src.main.date.calendar as calendar


class GrReference:
    """
    GR + 9 digits. First 4 digits are yymm, last 5 are the job number.
    """
    def __init__(self, date: Date = None, job_number: str = None):
        self._company_prefix = "GR"

        if job_number:
            if date:
                pass  # Not thought this out when both params used.

            else:
                self._set_full_job_number(job_number)

        else:
            if date:
                self._date = date

            else:
                self._date = calendar.current_month()

            self._job_number = "00000"

    def _set_full_job_number(self, job_number: str) -> None:
        digits = self._extract_digits_from_string(job_number)

        if not self._digits_are_valid_full_reference(digits):
            raise ValueError("Incorrect number of digits.")

        self._set_date_from_digits(digits)
        self._job_number = digits[-5:]

    @property
    def job_number(self):
        return self._job_number

    @job_number.setter
    def job_number(self, job_number: str):
        digits = self._extract_digits_from_string(job_number)

        if not self._digits_are_valid_job_number(digits):
            raise ValueError("Incorrect number of digits.")

        self._pad_job_number(digits)

    def _pad_job_number(self, brief_reference: str):
        # Needs edge case where date should be overwritten.
        self._job_number = (
            "0" * (5-len(brief_reference)) + brief_reference)

    def _set_date_from_digits(self, digits: str) -> None:
        year_digits = int(digits[0:2])
        month_digits = int(digits[2:4])

        self._date = calendar.date(month=month_digits, year=year_digits)

    @staticmethod
    def _digits_are_valid_full_reference(digits: str):
        return len(digits) == 9 and digits.isnumeric()

    @staticmethod
    def _digits_are_valid_job_number(digits: str):
        return 1 <= len(digits) <= 5 and digits.isnumeric()

    @staticmethod
    def _extract_digits_from_string(string: str):
        return re.sub("\\D", "", string)

    def to_string(self) -> str:
        return self._company_prefix + self._date.yymm() + self._job_number
