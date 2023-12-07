import date as calendar
from date import Date


class GrReference:
    """GR + 9 digits. First 4 digits: yymm; last 5 digits: job no."""

    def __init__(self, date: Date = None, job_number: str = None):
        self.prefix = "GR"

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

    def __str__(self) -> str:
        return self.prefix + self._date.format("yymm") + self._job_number

    def _set_full_job_number(self, job_number: str) -> None:
        digits = self._clean_job_number_candidate(job_number)

        if not len(digits) == 9 and digits.isnumeric():
            raise ValueError(f"Incorrect number of digits in {digits}.")

        self._date = calendar.date(int(digits[2:4]), int(digits[0:2]))
        self._job_number = digits[-5:]

    @property
    def job_number(self) -> str:
        return self._job_number

    @job_number.setter
    def job_number(self, job_number: str) -> None:
        digits = self._clean_job_number_candidate(job_number)
        digits_valid = 1 <= len(digits) <= 5 and digits.isnumeric()

        if not digits_valid:
            raise ValueError("Incorrect number of digits.")

        self._job_number = "0" * (5-len(digits)) + digits

    def _clean_job_number_candidate(self, job_number: str) -> str:
        return job_number.lower().removeprefix(self.prefix.lower()).strip()
