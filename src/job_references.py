from date import Calendar, Date


class GrReference:
    def __init__(self, date: Date = None, job_number: str = None) -> None:
        """GR + 9 digits. First 4 digits: yymm; last 5 digits: job no."""

        if not (date or job_number) or (date and job_number):
            raise ValueError("Must pass one parameter: date or job number.")

        self.prefix = "GR"

        if job_number:
            self._set_full_job_number(job_number)

        else:
            self._date = date
            self._job_number = "00000"

    def __str__(self) -> str:
        return self.prefix + self._date.format("yymm") + self._job_number

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

    def _set_full_job_number(self, job_number: str) -> None:
        digits = self._clean_job_number_candidate(job_number)

        if not len(digits) == 9 and digits.isnumeric():
            raise ValueError(f"Incorrect job reference format: {job_number}.")

        self._date = Calendar().date(int(digits[2:4]), int(digits[0:2]))
        self._job_number = digits[-5:]

    def _clean_job_number_candidate(self, job_number: str) -> str:
        return job_number.lower().removeprefix(self.prefix.lower()).strip()
    